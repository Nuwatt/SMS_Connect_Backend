import csv
from datetime import datetime

from django.db import IntegrityError
from django.db.models import F, Min, Max, Avg, OuterRef, Count, Subquery, Sum, Case, When
from django.db.models.functions import TruncMonth
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.localize.models import Country, City
from apps.snap.exceptions import PriceMonitorSnapNotFound
from apps.snap.models import (
    SnapChannel,
    SnapCategory,
    SnapBrand,
    SnapSKU,
    SnapPriceMonitor, SnapCountry
)


class PriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def __init__(self, sku_provided):
        self._sku_provided = sku_provided

    def _final_data(self, query):
        if not self._sku_provided:
            snap_skus = SnapSKU.objects.filter(is_archived=False).values('id')[:5]
            snap_ids = [item.get('id') for item in snap_skus]
            return query.filter(sku_id__in=snap_ids)
        return query


class GetPriceMonitorSnapUseCase(usecases.BaseUseCase):
    def __init__(self, price_monitor_snap_id: str):
        self._price_monitor_snap_id = price_monitor_snap_id

    def _factory(self):
        try:
            return SnapPriceMonitor.objects.get(pk=self._price_monitor_snap_id)
        except SnapPriceMonitor.DoesNotExist:
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

            snap, _snap_created = SnapPriceMonitor.objects.update_or_create(
                country_id=country_data[item.get('Country')].id,
                country_name=country_data[item.get('Country')].name,
                city_id=city_data[item.get('City')].id,
                city_name=city_data[item.get('City')].name,
                channel_id=channel_data[item.get('Channel')].id,
                channel_name=channel_data[item.get('Channel')].name,
                category_id=category_data[item.get('Category')].id,
                category_name=category_data[item.get('Category')].name,
                brand_id=brand_data[item.get('Brand')].id,
                brand_name=brand_data[item.get('Brand')].name,
                sku_id=sku_data[item.get('SKU')].id,
                sku_name=sku_data[item.get('SKU')].name,
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
    def __init__(self, filter_backends, request, view_self):
        self._view_self = view_self
        self._request = request
        self._filter_backends = filter_backends

    columns = [
        'Date', 'Country', 'City', 'Channel', 'Category', 'Brand',
        'SKU', 'Count', 'Mode', 'Mean', 'Max', 'Min'
    ]

    def _factory(self):
        response = HttpResponse(content_type='text/csv')
        filename = 'price_monitor_snap.csv'
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

        # 1. write headers
        writer = csv.writer(response)
        writer.writerow(self.columns)

        # 2. write questions
        queryset = SnapPriceMonitor.objects.unarchived().values(
            'date', 'country_name', 'city_name', 'channel_name', 'category_name',
            'brand_name', 'sku_name', 'count', 'mode', 'mean', 'max', 'min'
        )
        snaps = None
        for backend in list(self._filter_backends):
            snaps = backend().filter_queryset(self._request, queryset, self._view_self)

        for snap in snaps:
            writer.writerow([
                *snap.values()
            ])
        return response


class ListPriceMonitorSnapUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapPriceMonitor.objects.values(
            'city_name',
            'channel_name',
            'country_name',
            'category_name',
            'brand_name',
            'sku_name',
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
    def __init__(self, price_monitor_snap: SnapPriceMonitor):
        super().__init__(price_monitor_snap)


class UpdatePriceMonitorSnapUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, price_monitor_snap: SnapPriceMonitor):
        super().__init__(serializer, price_monitor_snap)


# class OverviewPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
#     def execute(self):
#         return self._factory()
#
#     def _factory(self):
#         snap_mode = PriceMonitorSnap.objects.filter(
#             sku=OuterRef('sku'),
#         ).values(
#             'mode',
#         ).order_by(
#             'created',
#         ).annotate(
#             frequency=Count('id')
#         ).order_by(
#             '-frequency',
#         ).values('mode')[:1]
#
#         return PriceMonitorSnap.objects.values(
#             'sku'
#         ).distinct().annotate(
#             sku_name=F('sku__name'),
#             min_value=Min('min'),
#             max_value=Max('max'),
#             mean_value=Avg('mean'),
#             mode_value=Subquery(snap_mode)
#         ).values(
#             'sku_name',
#             'min_value',
#             'max_value',
#             'mean_value',
#             'mode_value'
#         ).unarchived()


class OverviewPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        snap_mode = SnapPriceMonitor.objects.filter(
            sku_id=OuterRef('sku_id'),
        ).values(
            'mode',
        ).order_by(
            'created',
        ).annotate(
            frequency=Count('id')
        ).order_by(
            '-frequency',
        ).values('mode')[:1]

        query = SnapPriceMonitor.objects.values(
            'sku_id'
        ).distinct().annotate(
            min_value=Min('min'),
            max_value=Max('max'),
            mean_value=Avg('mean'),
            mode_value=Subquery(snap_mode)
        ).values(
            'sku_name',
            'sku_id',
            'min_value',
            'max_value',
            'mean_value',
            'mode_value'
        ).unarchived()

        return self._final_data(query)


class MonthMaxPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        query = SnapPriceMonitor.objects.values(
            'sku_id'
        ).distinct().annotate(
            month=TruncMonth('date'),
            value_max=Max('max'),
            value=Case(
                When(
                    value_max=None,
                    then=0,
                ),
                default=F('value_max')
            )
        ).values(
            'sku_name',
            'sku_id',
            'month',
            'value'
        ).unarchived()
        return self._final_data(query)


class MonthMinPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        query = SnapPriceMonitor.objects.values(
            'sku_id'
        ).distinct().annotate(
            month=TruncMonth('date'),
            value=Min('min'),
        ).values(
            'sku_name',
            'sku_id',
            'month',
            'value'
        ).unarchived()
        return self._final_data(query)


class MonthMeanPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        query = SnapPriceMonitor.objects.values(
            'sku_id'
        ).distinct().annotate(
            month=TruncMonth('date'),
            value=Avg('mean'),
        ).values(
            'sku_name',
            'sku_id',
            'month',
            'value'
        ).unarchived()
        return self._final_data(query)


class MonthModePriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        snap_mode = SnapPriceMonitor.objects.filter(
            sku_id=OuterRef('sku_id'),
        ).values(
            'mode',
        ).order_by(
            'created',
        ).annotate(
            frequency=Count('id')
        ).order_by(
            '-frequency',
        ).values('mode')[:1]

        query = SnapPriceMonitor.objects.values(
            'sku_id'
        ).distinct().annotate(
            month=TruncMonth('date'),
            value=Subquery(snap_mode)
        ).values(
            'month',
            'sku_name',
            'sku_id',
            'value'
        ).unarchived()
        return self._final_data(query)


class BrandOverviewPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def __init__(self, brand_provided):
        self._brand_provided = brand_provided

    def _final_data(self, query):
        if not self._brand_provided:
            snap_brands = SnapBrand.objects.filter(is_archived=False).values('id')[:5]
            snap_ids = [item.get('id') for item in snap_brands]
            return query.filter(brand_id__in=snap_ids)
        return query

    def _factory(self):
        snap_mode = SnapPriceMonitor.objects.filter(
            brand_id=OuterRef('brand_id'),
        ).values(
            'mode',
        ).order_by(
            'created',
        ).annotate(
            frequency=Count('id')
        ).order_by(
            '-frequency',
        ).values('mode')[:1]

        query = SnapPriceMonitor.objects.values(
            'brand_id'
        ).distinct().annotate(
            min_value=Min('min'),
            max_value=Max('max'),
            mean_value=Avg('mean'),
            mode_value=Subquery(snap_mode)
        ).values(
            'brand_name',
            'brand_id',
            'min_value',
            'max_value',
            'mean_value',
            'mode_value'
        ).unarchived()

        return self._final_data(query)


class CountryMinPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        query = SnapPriceMonitor.objects.values(
            'country_id',
        ).distinct().annotate(
            value=Min('min')
        ).values(
            'country_name',
            'sku_name',
            'sku_id',
            'value'
        ).unarchived()
        return self._final_data(query)


class CountryMaxPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        query = SnapPriceMonitor.objects.values(
            'country_id',
        ).distinct().annotate(
            value=Max('max')
        ).values(
            'country_name',
            'sku_name',
            'sku_id',
            'value'
        ).unarchived()
        return self._final_data(query)


class CountryMeanPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        query = SnapPriceMonitor.objects.values(
            'country_id',
        ).distinct().annotate(
            value=Avg('mean')
        ).values(
            'country_name',
            'sku_name',
            'sku_id',
            'value'
        ).unarchived()

        return self._final_data(query)


class CountryModePriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        snap_mode = SnapPriceMonitor.objects.filter(
            sku_id=OuterRef('sku_id'),
        ).values(
            'mode',
        ).order_by(
            'created',
        ).annotate(
            frequency=Count('id')
        ).order_by(
            '-frequency',
        ).values('mode')[:1]

        query = SnapPriceMonitor.objects.values(
            'sku_id'
        ).distinct().annotate(
            value=Subquery(snap_mode)
        ).values(
            'country_name',
            'sku_name',
            'sku_id',
            'value'
        ).unarchived()
        return self._final_data(query)


class VisitPerCityPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        query = SnapPriceMonitor.objects.values(
            'city_id'
        ).distinct().annotate(
            value=Sum('count')
        ).values(
            'city_name',
            'sku_name',
            'sku_id',
            'value'
        ).unarchived()
        return self._final_data(query)


class VisitPerCountryPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def __init__(self, country_provided):
        self._country_provided = country_provided

    def _final_data(self, query):
        if not self._country_provided:
            snap_countries = SnapCountry.objects.filter(is_archived=False).values('id')[:5]
            snap_ids = [item.get('id') for item in snap_countries]
            return query.filter(country_id__in=snap_ids)
        return query

    def _factory(self):
        query = SnapPriceMonitor.objects.values(
            'country_id'
        ).distinct().annotate(
            value=Sum('count')
        ).values(
            'country_name',
            'country_id',
            'value'
        ).unarchived()
        return self._final_data(query)


class SKUPerChannelPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        query = SnapPriceMonitor.objects.values(
            'channel_id'
        ).distinct().annotate(
            value=Sum('count')
        ).values(
            'channel_name',
            'sku_name',
            'sku_id',
            'value'
        ).unarchived()
        return self._final_data(query)


class BulkDeletePriceMonitorSnapUseCase(usecases.CreateUseCase):
    def _factory(self):
        SnapPriceMonitor.objects.filter(
            is_archived=False,
            id__in=self._data.get('snap_ids')
        ).archive()
