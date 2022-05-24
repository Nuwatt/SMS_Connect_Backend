import csv
from datetime import datetime

from django.db import IntegrityError
from django.db.models import Avg
from django.db.models import F, Sum
from django.db.models.functions import TruncMonth
from django.http import HttpResponse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.localize.models import Country, City
from apps.snap.exceptions import OutOfStockSnapNotFound
from apps.snap.models import (
    SnapOutOfStock,
    SnapChannel,
    SnapRetailer,
    SnapStore,
    SnapCategory,
    SnapBrand,
    SnapSKU, SnapCity
)


class GetOutOfStockSnapUseCase(usecases.BaseUseCase):
    def __init__(self, out_of_stock_snap_id: str):
        self._out_of_stock_snap_id = out_of_stock_snap_id

    def execute(self):
        self._factory()
        return self.out_of_stock_snap

    def _factory(self):
        try:
            self.out_of_stock_snap = SnapOutOfStock.objects.get(pk=self._out_of_stock_snap_id)
        except SnapOutOfStock.DoesNotExist:
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

            if item.get('Retailer') not in retailer_data:
                retailer, _retailer_created = SnapRetailer.objects.get_or_create(
                    name=item.get('Retailer').strip(),
                    is_archived=False
                )
                retailer_data[item.get('Retailer')] = retailer

            if item.get('Store') not in store_data:
                store, _store_created = SnapStore.objects.get_or_create(
                    name=item.get('Store').strip(),
                    channel=channel_data[item.get('Channel')],
                    retailer=retailer_data[item.get('Retailer')],
                    city=city_data[item.get('City')],
                    is_archived=False
                )
                store_data[item.get('Store')] = store

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

            snap, _snap_created = SnapOutOfStock.objects.update_or_create(
                city_id=city_data[item.get('City')].id,
                city_name=city_data[item.get('City')].name,
                country_id=country_data[item.get('Country')].id,
                country_name=country_data[item.get('Country')].name,
                channel_id=channel_data[item.get('Channel')].id,
                channel_name=channel_data[item.get('Channel')].name,
                category_id=category_data[item.get('Category')].id,
                category_name=category_data[item.get('Category')].name,
                brand_id=brand_data[item.get('Brand')].id,
                brand_name=brand_data[item.get('Brand')].name,
                sku_id=sku_data[item.get('SKU')].id,
                sku_name=sku_data[item.get('SKU')].name,
                store_id=store_data[item.get('Store')].id,
                store_name=store_data[item.get('Store')].name,
                date=datetime.strptime(item.get('Date'), "%Y-%m-%d").date(),
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
        return SnapOutOfStock.objects.values(
            'city_name',
            'country_name',
            'category_name',
            'brand_name',
            'sku_name',
            'channel_name',
            'retailer_name',
            'store_name',
            'count',
            'not_available_in_month',
            'less_available_in_month',
            'available_in_month',
            'not_available_by_store',
            'less_available_by_store',
            'available_by_store',
            'not_available_by_city',
            'less_available_by_city',
            'available_by_city',
            'id',
            'date',
            'created',
        ).unarchived()


class DeleteOutOfStockSnapUseCase(usecases.DeleteUseCase):
    def __init__(self, out_of_stock_snap: SnapOutOfStock):
        super().__init__(out_of_stock_snap)


class UpdateOutOfStockSnapUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, out_of_stock_snap: SnapOutOfStock):
        super().__init__(serializer, out_of_stock_snap)


class OutOfStockSnapReportUseCase(usecases.BaseUseCase):
    def __init__(self, sku_provided):
        self._sku_provided = sku_provided

    def _final_data(self, query):
        if not self._sku_provided:
            snap_skus = SnapSKU.objects.filter(is_archived=False).values('id')[:5]
            snap_ids = [item.get('id') for item in snap_skus]
            return query.filter(sku_id__in=snap_ids)
        return query


class OverviewOutOfStockSnapReportUseCase(OutOfStockSnapReportUseCase):
    def _factory(self):
        query = SnapOutOfStock.objects.values(
            'sku_id'
        ).distinct().annotate(
            available=Avg('available_in_month'),
            not_available=Avg('not_available_in_month'),
            less=Avg('less_available_in_month'),
        ).values(
            'sku_name',
            'sku_id',
            'available',
            'not_available',
            'less'
        ).unarchived()
        return self._final_data(query)


class AvailableOutOfStockSnapReportUseCase(OutOfStockSnapReportUseCase):
    def _factory(self):
        query = SnapOutOfStock.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).distinct().annotate(
            value=Avg('available_in_month'),
        ).values(
            'month',
            'sku_name',
            'sku_id',
            'value'
        ).unarchived()
        return self._final_data(query)


class NotAvailableOutOfStockSnapReportUseCase(OutOfStockSnapReportUseCase):
    def _factory(self):
        query = SnapOutOfStock.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).distinct().annotate(
            value=Avg('not_available_in_month'),
        ).values(
            'month',
            'sku_name',
            'sku_id',
            'value'
        ).unarchived()
        return self._final_data(query)


class LessOutOfStockSnapReportUseCase(OutOfStockSnapReportUseCase):
    def _factory(self):
        query = SnapOutOfStock.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).distinct().annotate(
            value=Avg('less_available_in_month'),
        ).values(
            'month',
            'sku_name',
            'sku_id',
            'value'
        ).unarchived()
        return self._final_data(query)


# city
class AvailableByCityOutOfStockSnapReportUseCase(OutOfStockSnapReportUseCase):
    def _factory(self):
        query = SnapOutOfStock.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).distinct().annotate(
            value=Avg('available_in_month'),
        ).values(
            'city_name',
            'month',
            'sku_name',
            'sku_id',
            'value'
        ).unarchived()
        return self._final_data(query)


class NotAvailableByCityOutOfStockSnapReportUseCase(OutOfStockSnapReportUseCase):
    def _factory(self):
        query = SnapOutOfStock.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).distinct().annotate(
            value=Avg('not_available_in_month'),
        ).values(
            'city_name',
            'month',
            'sku_name',
            'sku_id',
            'value'
        ).unarchived()
        return self._final_data(query)


class LessByCityOutOfStockSnapReportUseCase(OutOfStockSnapReportUseCase):
    def _factory(self):
        query = SnapOutOfStock.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).distinct().annotate(
            value=Avg('less_available_in_month'),
        ).values(
            'city_name',
            'month',
            'sku_name',
            'sku_id',
            'value'
        ).unarchived()
        return self._final_data(query)


class VisitByCityOutOfStockSnapReportUseCase(usecases.BaseUseCase):
    def __init__(self, city_provided):
        self._city_provided = city_provided

    def _final_data(self, query):
        if not self._city_provided:
            snap_cities = SnapCity.objects.filter(is_archived=False).values('id')[:5]
            snap_ids = [item.get('id') for item in snap_cities]
            return query.filter(sku_id__in=snap_ids)
        return query

    def _factory(self):
        query = SnapOutOfStock.objects.values(
            'city_id'
        ).distinct().annotate(
            value=Sum('count'),
        ).values(
            'city_name',
            'city_id',
            'value'
        ).unarchived()
        return self._final_data(query)


class NotAvailableByWeekOutOfStockSnapReportUseCase(OutOfStockSnapReportUseCase):
    def _factory(self):
        current_week = now().isocalendar()[1]
        query = SnapOutOfStock.objects.filter(
            not_available_by_store__gt=0
        ).values(
            'sku_id'
        ).distinct().annotate(
            week=F('date'),
        ).values(
            'week',
            'sku_name',
            'sku_id',
            'store_name',
            'retailer_name'
        ).unarchived()
        return self._final_data(query)


class BulkDeleteOutOfStockSnapUseCase(usecases.CreateUseCase):
    def _factory(self):
        SnapOutOfStock.objects.filter(
            is_archived=False,
            id__in=self._data.get('snap_ids')
        ).archive()


class ExportOutOfStockSnapUseCase(usecases.BaseUseCase):
    def __init__(self, filter_backends, request, view_self):
        self._view_self = view_self
        self._request = request
        self._filter_backends = filter_backends

    columns = [
        'Date', 'Country', 'City', 'Channel', 'Retailer', 'Store',
        'Category', 'Brand', 'SKU', 'Count', 'Not Available In Month',
        'Less Available In Month', 'Available In Month', 'Not Available By Store',
        'Less Available By Store', 'Available By Store', 'Not Available By City',
        'Less Available By City', 'Available By City'
    ]

    def _factory(self):
        response = HttpResponse(content_type='text/csv')
        filename = 'out_of_stock_snap.csv'
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

        # 1. write headers
        writer = csv.writer(response)
        writer.writerow(self.columns)

        # 2. write questions
        queryset = SnapOutOfStock.objects.unarchived().values(
            'date', 'country_name', 'city_name', 'channel_name',
            'retailer_name', 'store_name', 'category_name',
            'brand_name', 'sku_name', 'count', 'not_available_in_month',
            'less_available_in_month', 'available_in_month',
            'not_available_by_store', 'less_available_by_store',
            'available_by_store', 'not_available_by_city',
            'less_available_by_city', 'available_by_city',
        )
        snaps = None
        for backend in list(self._filter_backends):
            snaps = backend().filter_queryset(self._request, queryset, self._view_self)
        for snap in snaps:
            writer.writerow([
                *snap.values()
            ])
        return response


class OutOfStockSnapCityReportUseCase(OutOfStockSnapReportUseCase):
    def _factory(self):
        query = SnapOutOfStock.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).distinct().annotate(
            not_available_by_city_value=Avg('not_available_by_city'),
            less_available_by_city_value=Avg('less_available_by_city'),
            available_by_city_value=Avg('available_by_city'),
        ).values(
            'city_name',
            'month',
            'sku_name',
            'sku_id',
            'not_available_by_city_value',
            'less_available_by_city_value',
            'available_by_city_value'
        ).unarchived()
        return self._final_data(query)


class OutOfStockSnapCityChannelReportUseCase(OutOfStockSnapReportUseCase):
    def _factory(self):
        query = SnapOutOfStock.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).annotate(
            not_available_by_city_value=Avg('not_available_by_city'),
            less_available_by_city_value=Avg('less_available_by_city'),
            available_by_city_value=Avg('available_by_city'),
        ).values(
            'month',
            'city_name',
            'channel_name',
            'sku_name',
            'sku_id',
            'not_available_by_city_value',
            'less_available_by_city_value',
            'available_by_city_value'
        ).unarchived()
        return self._final_data(query)


class OutOfStockSnapStoreReportUseCase(usecases.BaseUseCase):
    def __init__(self, store_provided, sku_provided):
        self._sku_provided = sku_provided
        self._store_provided = store_provided

    def _final_data(self, query):
        if not self._store_provided and not self._sku_provided:
            snap_stores = SnapStore.objects.filter(is_archived=False).values('id')[:5]
            snap_skus = SnapSKU.objects.filter(is_archived=False).values('id')[:5]
            snap_ids = [item.get('id') for item in snap_stores]
            sku_ids = [item.get('id') for item in snap_skus]
            return query.filter(store_id__in=snap_ids, sku_id__in=sku_ids)
        elif not self._store_provided:
            snap_stores = SnapStore.objects.filter(is_archived=False).values('id')[:5]
            snap_ids = [item.get('id') for item in snap_stores]
            return query.filter(store_id__in=snap_ids)
        return query

    def _factory(self):
        query = SnapOutOfStock.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).distinct().annotate(
            not_available_by_store_value=Avg('not_available_by_store'),
            less_available_by_store_value=Avg('less_available_by_store'),
            available_by_store_value=Avg('available_by_store'),
        ).values(
            'store_name',
            'month',
            'sku_name',
            'sku_id',
            'not_available_by_store_value',
            'less_available_by_store_value',
            'available_by_store_value'
        ).unarchived()
        return self._final_data(query)


class OutOfStockSnapMonthReportUseCase(OutOfStockSnapReportUseCase):
    def _factory(self):
        query = SnapOutOfStock.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).distinct().annotate(
            not_available_by_month_value=Avg('not_available_in_month'),
            less_available_by_month_value=Avg('less_available_in_month'),
            available_by_month_value=Avg('available_in_month'),
        ).values(
            'month',
            'sku_name',
            'sku_id',
            'not_available_by_month_value',
            'less_available_by_month_value',
            'available_by_month_value'
        ).unarchived()
        return self._final_data(query)
