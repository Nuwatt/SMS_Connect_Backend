from datetime import datetime

from django.db import IntegrityError
from django.db.models import F, Min, Max, Avg, OuterRef, Count, Subquery, Sum
from django.db.models.functions import TruncMonth, ExtractWeek
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.localize.models import Country, City
from apps.market.models import Channel, Retailer, Store
from apps.product.models import Category, Brand, SKU
from apps.snap.exceptions import OutOfStockSnapNotFound
from apps.snap.models import OutOfStockSnap


class GetOutOfStockSnapUseCase(usecases.BaseUseCase):
    def __init__(self, out_of_stock_snap_id: str):
        self._out_of_stock_snap_id = out_of_stock_snap_id

    def execute(self):
        self._factory()
        return self.out_of_stock_snap

    def _factory(self):
        try:
            self.out_of_stock_snap = OutOfStockSnap.objects.get(pk=self._out_of_stock_snap_id)
        except OutOfStockSnap.DoesNotExist:
            raise OutOfStockSnapNotFound


class ImportOutOfStockSnapUseCase(usecases.ImportCSVUseCase):
    def __init__(self, serializer):
        super().__init__(serializer)

    valid_columns = ['Date', 'Country', 'City', 'Channel', 'Retailer',
                     'Store', 'Category', 'Brand', 'SKU', 'Count',
                     'Not Available In Month', 'Less Available In Month', 'Available In Month',
                     'Not Available By Store', 'Less Available By Store', 'Available By Store',
                     'Not Available By City', 'Less Available By City', 'Available By City']

    def _factory(self):
        country_data = {}
        city_data = {}
        channel_data = {}
        retailer_data = {}
        store_data = {}
        category_data = {}
        brand_data = {}
        sku_data = {}

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

            if item.get('Retailer') not in retailer_data:
                retailer, _created = Retailer.objects.get_or_create(
                    name=item.get('Retailer'),
                    is_archived=False
                )
                retailer_data[item.get('Retailer')] = retailer

            if item.get('Store') not in store_data:
                store, _created = Store.objects.get_or_create(
                    name=item.get('Store'),
                    channel=channel_data[item.get('Channel')],
                    retailer=retailer_data[item.get('Retailer')],
                    is_archived=False
                )
                store_data[item.get('Store')] = store

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

            if item.get('SKU') not in sku_data:
                sku, _created = SKU.objects.get_or_create(
                    name=item.get('SKU'),
                    brand=brand_data[item.get('Brand')],
                    category=category_data[item.get('Category')],
                    is_archived=False
                )
                sku_data[item.get('SKU')] = sku

            snap, _created = OutOfStockSnap.objects.update_or_create(
                city=city_data[item.get('City')],
                store=store_data[item.get('Store')],
                sku=sku_data[item.get('SKU')],
                date=datetime.strptime(item.get('Date'), "%m/%d/%Y").date(),
                defaults={
                    'count': item.get('Count'),
                    'not_available_in_month': item.get('Not Available In Month'),
                    'less_available_in_month': item.get('Less Available In Month'),
                    'available_in_month': item.get('Available In Month'),
                    'not_available_by_store': item.get('Not Available By Store'),
                    'less_available_by_store': item.get('Less Available By Store'),
                    'available_by_store': item.get('Available By Store'),
                    'not_available_by_city': item.get('Not Available By City'),
                    'less_available_by_city': item.get('Less Available By City'),
                    'available_by_city': item.get('Available By City')
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


class ListOutOfStockSnapUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return OutOfStockSnap.objects.select_related(
            'city',
            'city__country',
            'sku__category',
            'sku__brand',
            'sku',
            'store__channel',
            'store__retailer',
            'store',
        ).unarchived()


class DeleteOutOfStockSnapUseCase(usecases.DeleteUseCase):
    def __init__(self, out_of_stock_snap: OutOfStockSnap):
        super().__init__(out_of_stock_snap)


class UpdatePriceMonitorSnapUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, out_of_stock_snap: OutOfStockSnap):
        super().__init__(serializer, out_of_stock_snap)


class OverviewOutOfStockSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return OutOfStockSnap.objects.values(
            'sku'
        ).distinct().annotate(
            sku_name=F('sku__name'),
            available=F('available_in_month'),
            not_available=F('not_available_in_month'),
            less=F('less_available_in_month'),
        ).values(
            'sku_name',
            'available',
            'not_available',
            'less'
        ).unarchived()


class AvailableOutOfStockSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return OutOfStockSnap.objects.annotate(
            month=TruncMonth('date'),
            value=F('available_in_month'),
            sku_name=F('sku__name')
        ).values(
            'month',
            'sku_name',
            'value'
        ).unarchived().filter(
            value__gt=0
        )


class NotAvailableOutOfStockSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return OutOfStockSnap.objects.annotate(
            month=TruncMonth('date'),
            value=F('not_available_in_month'),
            sku_name=F('sku__name')
        ).values(
            'month',
            'sku_name',
            'value'
        ).unarchived().filter(
            value__gt=0
        )


class LessOutOfStockSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return OutOfStockSnap.objects.annotate(
            month=TruncMonth('date'),
            value=F('less_available_in_month'),
            sku_name=F('sku__name')
        ).values(
            'month',
            'sku_name',
            'value'
        ).unarchived().filter(
            value__gt=0
        )


# city
class AvailableByCityOutOfStockSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return OutOfStockSnap.objects.annotate(
            city_name=F('city__name'),
            value=F('available_in_month'),
            sku_name=F('sku__name')
        ).values(
            'city_name',
            'sku_name',
            'value'
        ).unarchived().filter(
            value__gt=0
        )


class NotAvailableByCityOutOfStockSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return OutOfStockSnap.objects.annotate(
            city_name=F('city__name'),
            value=F('not_available_in_month'),
            sku_name=F('sku__name')
        ).values(
            'city_name',
            'sku_name',
            'value'
        ).unarchived().filter(
            value__gt=0
        )


class LessByCityOutOfStockSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return OutOfStockSnap.objects.annotate(
            city_name=F('city__name'),
            value=F('less_available_in_month'),
            sku_name=F('sku__name')
        ).values(
            'city_name',
            'sku_name',
            'value'
        ).unarchived().filter(
            value__gt=0
        )


class VisitByCityOutOfStockSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return OutOfStockSnap.objects.values(
            'city'
        ).distinct().annotate(
            city_name=F('city__name'),
            value=Sum('count'),
        ).values(
            'city_name',
            'value'
        ).unarchived()


class NotAvailableByWeekOutOfStockSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        current_week = now().isocalendar()[1]
        return OutOfStockSnap.objects.filter(
            not_available_by_store__gt=0
        ).values(
            'sku'
        ).distinct().annotate(
            completed_week=ExtractWeek('date'),
            week=current_week - F('completed_week'),
            sku_name=F('sku__name'),
            store_name=F('store__name'),
            retailer_name=F('store__retailer__name'),
        ).values(
            'week',
            'sku_name',
            'store_name',
            'retailer_name'
        ).unarchived()
