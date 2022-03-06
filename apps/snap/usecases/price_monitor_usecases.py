import csv
from datetime import datetime

from django.db import IntegrityError
from django.db.models import F, Min, Max, Avg, OuterRef, Count, Subquery, Sum, Q
from django.db.models.functions import TruncMonth
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.localize.models import Country, City
from apps.snap.exceptions import PriceMonitorSnapNotFound
from apps.snap.models import PriceMonitorSnap, SnapChannel, SnapCategory, SnapBrand, SnapSKU


class GetPriceMonitorSnapUseCase(usecases.BaseUseCase):
    def __init__(self, price_monitor_snap_id: str):
        self._price_monitor_snap_id = price_monitor_snap_id

    def execute(self):
        self._factory()
        return self._price_monitor_snap

    def _factory(self):
        try:
            self._price_monitor_snap = PriceMonitorSnap.objects.get(pk=self._price_monitor_snap_id)
        except PriceMonitorSnap.DoesNotExist:
            raise PriceMonitorSnapNotFound


class ImportPriceMonitorSnapUseCase(usecases.ImportCSVUseCase):
    def __init__(self, serializer):
        super().__init__(serializer)

    valid_columns = ['Date', 'Country', 'City', 'Channel', 'Category', 'Brand',
                     'SKU', 'Count', 'Mode', 'Mean', 'Max', 'Min']

    def _factory(self):
        country_data = {}
        city_data = {}
        channel_data = {}
        category_data = {}
        brand_data = {}
        sku_data = {}

        for item in self._item_list:
            if item.get('Country') not in country_data:
                country, _country_created = Country.objects.get_or_create(
                    name=item.get('Country').strip(),
                    is_archived=False
                )
                country_data[item.get('Country')] = country

            if item.get('City') not in city_data:
                city, _city_created = City.objects.get_or_create(
                    name=item.get('City').strip(),
                    country=country_data[item.get('Country')],
                    is_archived=False
                )
                city_data[item.get('City')] = city

            if item.get('Channel') not in channel_data:
                channel, _channel_created = SnapChannel.objects.get_or_create(
                    name=item.get('Channel').strip(),
                    is_archived=False
                )
                channel_data[item.get('Channel')] = channel

            if item.get('Category') not in category_data:
                category, _category_created = SnapCategory.objects.get_or_create(
                    name=item.get('Category').strip(),
                    is_archived=False
                )
                category_data[item.get('Category')] = category

            if item.get('Brand') not in brand_data:
                brand, _brand_created = SnapBrand.objects.get_or_create(
                    name=item.get('Brand').strip(),
                    is_archived=False
                )
                brand_data[item.get('Brand')] = brand

            if item.get('SKU') not in sku_data:
                sku, _sku_created = SnapSKU.objects.get_or_create(
                    name=item.get('SKU').strip(),
                    brand=brand_data[item.get('Brand')],
                    category=category_data[item.get('Category')],
                    is_archived=False
                )
                sku_data[item.get('SKU')] = sku
                sku.country.add(country_data[item.get('Country')])

            snap, _snap_created = PriceMonitorSnap.objects.update_or_create(
                city=city_data[item.get('City')],
                channel=channel_data[item.get('Channel')],
                sku=sku_data[item.get('SKU')],
                date=datetime.strptime(item.get('Date'), "%Y-%m-%d").date(),
                defaults={
                    'count': item.get('Count'),
                    'mode': item.get('Mode'),
                    'mean': item.get('Mean'),
                    'max': item.get('Max'),
                    'min': item.get('Min')
                }
            )

    def execute(self):
        self.is_valid()
        try:
            self._factory()
        except IntegrityError as e:
            print(e)
            raise ValidationError({
                'non_field_errors': _('CSV Contains invalid ids.')
            })


class ExportPriceMonitorSnapUseCase(usecases.BaseUseCase):
    columns = [
        'Date', 'Country', 'City', 'Channel', 'Category', 'Brand',
        'SKU', 'Count', 'Mode', 'Mean', 'Max', 'Min'
    ]

    def execute(self):
        return self._factory()

    def _factory(self):
        response = HttpResponse(content_type='text/csv')
        filename = 'price_monitor_snap.csv'
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

        # 1. write headers
        writer = csv.writer(response)
        writer.writerow(self.columns)

        # 2. write questions
        snaps = PriceMonitorSnap.objects.unarchived().values(
            'date', 'city__country__name', 'city__name', 'channel__name', 'sku__category__name',
            'sku__brand__name', 'sku__name', 'count', 'mode', 'mean', 'max', 'min'
        )
        for snap in snaps:
            writer.writerow([
                *snap.values()
            ])
        return response


class ListPriceMonitorSnapUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return PriceMonitorSnap.objects.values(
            'city__name',
            'channel__name',
            'city__country__name',
            'sku__category__name',
            'sku__brand__name',
            'sku__brand__name',
            'sku__name',
            'count',
            'date',
            'id',
            'min',
            'min',
            'max',
            'mean',
            'mode',
            'created'
        ).unarchived()


class DeletePriceMonitorSnapUseCase(usecases.DeleteUseCase):
    def __init__(self, price_monitor_snap: PriceMonitorSnap):
        super().__init__(price_monitor_snap)


class UpdatePriceMonitorSnapUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, price_monitor_snap: PriceMonitorSnap):
        super().__init__(serializer, price_monitor_snap)


class OverviewPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        snap_mode = PriceMonitorSnap.objects.filter(
            sku=OuterRef('sku'),
        ).values(
            'mode',
        ).order_by(
            'created',
        ).annotate(
            frequency=Count('id')
        ).order_by(
            '-frequency',
        ).values('mode')[:1]

        return PriceMonitorSnap.objects.values(
            'sku'
        ).distinct().annotate(
            sku_name=F('sku__name'),
            min_value=Min('min'),
            max_value=Max('max'),
            mean_value=Avg('mean'),
            mode_value=Subquery(snap_mode)
        ).values(
            'sku_name',
            'min_value',
            'max_value',
            'mean_value',
            'mode_value'
        ).unarchived()


class MonthMaxPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        # return PriceMonitorSnap.objects.annotate(
        #     month=TruncMonth('date'),
        #     value=F('max'),
        #     sku_name=F('sku__name')
        # ).values(
        #     'month',
        #     'sku_name',
        #     'value'
        # ).unarchived()
        return PriceMonitorSnap.objects.values(
            'sku'
        ).distinct().annotate(
            month=TruncMonth('date'),
            sku_name=F('sku__name'),
            values=Max('max'),
            
        ).values(
            'sku_name',
            'month',
            'value'
        ).unarchived()


class MonthMinPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        # return PriceMonitorSnap.objects.annotate(
        #     month=TruncMonth('date'),
        #     value=F('min'),
        #     sku_name=F('sku__name')
        # ).values(
        #     'month',
        #     'sku_name',
        #     'value'
        # ).unarchived()

        return PriceMonitorSnap.objects.values(
            'sku'
        ).distinct().annotate(
            month=TruncMonth('date'),
            sku_name=F('sku__name'),
            value=Min('min'),
        ).values(
            'sku_name',
            'month',
            'value'
        ).unarchived()


class MonthMeanPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        # return PriceMonitorSnap.objects.annotate(
        #     month=TruncMonth('date'),
        #     value=F('mean'),
        #     sku_name=F('sku__name')
        # ).values(
        #     'month',
        #     'sku_name',
        #     'value'
        # ).unarchived()

        return PriceMonitorSnap.objects.values(
            'sku'
        ).distinct().annotate(
            month=TruncMonth('date'),
            sku_name=F('sku__name'),
            value=Avg('mean'),
        ).values(
            'sku_name',
            'month',
            'value'
        ).unarchived()


class MonthModePriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        # return PriceMonitorSnap.objects.annotate(
        #     month=TruncMonth('date'),
        #     value=F('mode'),
        #     sku_name=F('sku__name')
        # ).values(
        #     'month',
        #     'sku_name',
        #     'value'
        # ).unarchived()

        snap_mode = PriceMonitorSnap.objects.filter(
            sku=OuterRef('sku'),
        ).values(
            'mode',
        ).order_by(
            'created',
        ).annotate(
            frequency=Count('id')
        ).order_by(
            '-frequency',
        ).values('mode')[:1]

        return PriceMonitorSnap.objects.values(
            'sku'
        ).distinct().annotate(
            month=TruncMonth('date'),
            sku_name=F('sku__name'),
            value=Subquery(snap_mode)
        ).values(
            'month',
            'sku_name',
            'value'
        ).unarchived()


class BrandOverviewPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def _factory(self):
        # snap_mode = PriceMonitorSnap.objects.filter(
        #     sku__brand=OuterRef('sku__brand'),
        # ).values(
        #     'mode',
        # ).order_by(
        #     'date',
        # ).annotate(
        #     frequency=Count('mode')
        # ).order_by(
        #     '-frequency'
        # ).values('mode')[:1]

        return PriceMonitorSnap.objects.unarchived()


class CountryMinPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return PriceMonitorSnap.objects.annotate(
            country=F('city__country')
        ).values(
            'country',
        ).annotate(
            country_name=F('city__country__name'),
            sku_name=F('sku__name'),
            value=Min('min')
        ).values(
            'country_name',
            'sku_name',
            'value'
        ).unarchived()


class CountryMaxPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return PriceMonitorSnap.objects.annotate(
            country=F('city__country')
        ).values(
            'country',
        ).annotate(
            country_name=F('city__country__name'),
            sku_name=F('sku__name'),
            value=self.null_validate(Max('max'))
        ).values(
            'country_name',
            'sku_name',
            'value'
        ).unarchived()


class CountryMeanPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return PriceMonitorSnap.objects.annotate(
            country=F('city__country')
        ).values(
            'country',
        ).annotate(
            country_name=F('city__country__name'),
            sku_name=F('sku__name'),
            value=Avg('mean')
        ).values(
            'country_name',
            'sku_name',
            'value'
        ).unarchived()


class CountryModePriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        snap_mode = PriceMonitorSnap.objects.filter(
            sku=OuterRef('sku'),
        ).values(
            'mode',
        ).order_by(
            'created',
        ).annotate(
            frequency=Count('id')
        ).order_by(
            '-frequency',
        ).values('mode')[:1]

        return PriceMonitorSnap.objects.values(
            'sku'
        ).distinct().annotate(
            country_name=F('city__country__name'),
            sku_name=F('sku__name'),
            value=Subquery(snap_mode)
        ).values(
            'country_name',
            'sku_name',
            'value'
        ).unarchived()


class VisitPerCityPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return PriceMonitorSnap.objects.values(
            'city'
        ).distinct().annotate(
            city_name=F('city__name'),
            sku_name=F('sku__name'),
            value=Sum('count')
        ).values(
            'city_name',
            'sku_name',
            'value'
        ).unarchived()


class VisitPerCountryPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return PriceMonitorSnap.objects.values(
            'city__country'
        ).distinct().annotate(
            country_name=F('city__country__name'),
            value=Sum('count')
        ).values(
            'country_name',
            'value'
        ).unarchived()


class SKUPerChannelPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return PriceMonitorSnap.objects.values(
            'channel'
        ).distinct().annotate(
            sku_name=F('sku__name'),
            channel_name=F('channel__name'),
            value=Sum('count')
        ).values(
            'channel_name',
            'sku_name',
            'value'
        ).unarchived()


class BulkDeletePriceMonitorSnapUseCase(usecases.CreateUseCase):
    def _factory(self):
        PriceMonitorSnap.objects.filter(
            is_archived=False,
            id__in=self._data.get('snap_ids')
        ).archive()
