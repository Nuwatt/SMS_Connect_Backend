from datetime import datetime

from django.db import IntegrityError
from django.db.models import F, Min, Max, Avg, OuterRef, Count, Subquery
from django.db.models.functions import TruncMonth
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.localize.models import Country, City
from apps.market.models import Channel
from apps.product.models import Category, Brand
from apps.snap.exceptions import PriceMonitorSnapNotFound
from apps.snap.models import PriceMonitorSnap


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

        for item in self._item_list:
            if item.get('Country') not in country_data:
                country, _created = Country.objects.get_or_create(
                    name=item.get('Country'),
                    is_archived=False
                )
                country_data[item.get('Country')] = country

            if item.get('City') not in country_data:
                city, _created = City.objects.get_or_create(
                    name=item.get('City'),
                    country=country_data[item.get('Country')],
                    is_archived=False
                )
                city_data[item.get('City')] = city

            if item.get('Channel') not in channel_data:
                channel, _created = Channel.objects.get_or_create(
                    name=item.get('Channel'),
                    is_archived=False
                )
                channel_data[item.get('Channel')] = channel

            if item.get('Category') not in category_data:
                category, _created = Category.objects.get_or_create(
                    name=item.get('Category'),
                    is_archived=False
                )
                category_data[item.get('Category')] = category

            if item.get('Brand') not in brand_data:
                brand, _created = Brand.objects.get_or_create(
                    name=item.get('Brand'),
                    is_archived=False
                )
                brand_data[item.get('Brand')] = brand

            snap, _created = PriceMonitorSnap.objects.update_or_create(
                city=city_data[item.get('City')],
                channel=channel_data[item.get('Channel')],
                category=category_data[item.get('Category')],
                brand=brand_data[item.get('Brand')],
                sku=item.get('SKU'),
                date=datetime.strptime(item.get('Date'), "%m/%d/%Y").date(),
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


class ListPriceMonitorSnapUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return PriceMonitorSnap.objects.select_related(
            'city',
            'channel',
            'city__country',
            'category',
            'brand',
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
        return PriceMonitorSnap.objects.unarchived()


class MonthMaxPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return PriceMonitorSnap.objects.annotate(
            month=TruncMonth('date'),
            value=F('max')
        ).values(
            'month',
            'sku',
            'value'
        ).unarchived()


class MonthMinPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return PriceMonitorSnap.objects.annotate(
            month=TruncMonth('date'),
            value=F('min')
        ).values(
            'month',
            'sku',
            'value'
        ).unarchived()


class MonthMeanPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return PriceMonitorSnap.objects.annotate(
            month=TruncMonth('date'),
            value=F('mean')
        ).values(
            'month',
            'sku',
            'value'
        ).unarchived()


class MonthModePriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return PriceMonitorSnap.objects.annotate(
            month=TruncMonth('date'),
            value=F('mode')
        ).values(
            'month',
            'sku',
            'value'
        ).unarchived()


class BrandOverviewPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        snap_mode = PriceMonitorSnap.objects.filter(
            brand=OuterRef('brand'),
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
            'brand'
        ).distinct().annotate(
            brand_name=F('brand__name'),
            min_value=Min('min'),
            max_value=Max('max'),
            mean_value=Avg('mean'),
            mode_value=Subquery(snap_mode)
        ).unarchived()
