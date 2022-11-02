import csv
from datetime import datetime

from django.db import IntegrityError
from django.db.models import Sum, Avg
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.snap.exceptions import DistributionSnapNotFound
from apps.snap.models import (
    SnapDistribution,
    SnapChannel,
    SnapCategory,
    SnapBrand,
    SnapSKU, SnapCountry, SnapCity
)


class GetDistributionSnapUseCase(usecases.BaseUseCase):
    def __init__(self, distribution_snap_id: str):
        self._distribution_snap_id = distribution_snap_id

    def _factory(self):
        try:
            return SnapDistribution.objects.get(pk=self._distribution_snap_id)
        except SnapDistribution.DoesNotExist:
            raise DistributionSnapNotFound


class ImportDistributionSnapUseCase(usecases.ImportCSVUseCase):
    def __init__(self, serializer):
        super().__init__(serializer)

    valid_columns = [
        'Date', 'Country', 'City', 'Channel', 'Category', 'Brand', 'SKU',
        'Total Distribution', 'Shelf Share', 'Number Of Outlet'
    ]

    def _factory(self):
        country_data = {}
        city_data = {}
        channel_data = {}
        category_data = {}
        brand_data = {}
        sku_data = {}

        for item in self._item_list:
            if item.get('Country') not in country_data:
                country, _created = SnapCountry.objects.get_or_create(
                    name=item.get('Country').strip(),
                    is_archived=False
                )
                country_data[item.get('Country')] = country

            if item.get('City') not in country_data:
                city, _created = SnapCity.objects.get_or_create(
                    name=item.get('City').strip(),
                    country=country_data[item.get('Country')],
                    is_archived=False
                )
                city_data[item.get('City')] = city

            if item.get('Channel') not in channel_data:
                channel, _created = SnapChannel.objects.get_or_create(
                    name=item.get('Channel').strip(),
                    is_archived=False
                )
                channel_data[item.get('Channel')] = channel

            if item.get('Category') not in category_data:
                category, _created = SnapCategory.objects.get_or_create(
                    name=item.get('Category').strip(),
                    is_archived=False
                )
                category_data[item.get('Category')] = category

            if item.get('Brand') not in brand_data:
                brand, _created = SnapBrand.objects.get_or_create(
                    name=item.get('Brand').strip(),
                    is_archived=False
                )
                brand_data[item.get('Brand')] = brand

            if item.get('SKU') not in sku_data:
                sku, _created = SnapSKU.objects.get_or_create(
                    name=item.get('SKU').strip(),
                    brand=brand_data[item.get('Brand')],
                    category=category_data[item.get('Category')],
                    is_archived=False
                )
                sku_data[item.get('SKU')] = sku

            snap, _created = SnapDistribution.objects.update_or_create(
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
                date=datetime.strptime(item.get('Date'), "%Y-%m-%d").date(),
                is_archived=False,
                defaults={
                    'total_distribution': item.get('Total Distribution'),
                    'shelf_share': item.get('Shelf Share'),
                    'number_of_outlet': item.get('Number Of Outlet'),
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


class ListDistributionSnapUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapDistribution.objects.values(
            'city_name',
            'country_name',
            'category_name',
            'brand_name',
            'sku_name',
            'channel_name',
            'id',
            'created',
            'date',
            'total_distribution',
            'shelf_share',
            'number_of_outlet'
        ).unarchived()


class DeleteDistributionSnapUseCase(usecases.DeleteUseCase):
    def __init__(self, price_monitor_snap: SnapDistribution):
        super().__init__(price_monitor_snap)


class UpdateDistributionSnapUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, price_monitor_snap: SnapDistribution):
        super().__init__(serializer, price_monitor_snap)


class VisitByCountryDistributionSnapReportUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapDistribution.objects.values(
            'country_id'
        ).distinct().annotate(
            value=Sum('count'),
        ).values(
            'country_name',
            'value'
        ).unarchived()


class VisitByCityDistributionSnapReportUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapDistribution.objects.values(
            'city_id'
        ).distinct().annotate(
            value=Sum('count'),
        ).values(
            'city_name',
            'value'
        ).unarchived()


class VisitByChannelDistributionSnapReportUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapDistribution.objects.values(
            'channel_id'
        ).distinct().annotate(
            value=Sum('count'),
        ).values(
            'channel_name',
            'value'
        ).unarchived()


class SKUByCityDistributionSnapReportUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapDistribution.objects.values(
            'city_id'
        ).distinct().annotate(
            value=Sum('sku_by_city'),
        ).values(
            'city_name',
            'sku_name',
            'value'
        ).unarchived()


class TotalDistributionSnapReportUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapDistribution.objects.values(
            'sku_id'
        ).distinct().annotate(
            value=Avg('total_distribution')
        ).values(
            'value',
            'sku_name',
        ).unarchived()


class ShelfShareDistributionSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return SnapDistribution.objects.values(
            'sku_id'
        ).distinct().annotate(
            value=Avg('shelf_share')
        ).values(
            'value',
            'city_name',
            'sku_name',
        ).unarchived()


class NumberOfOutletDistributionSnapReportUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapDistribution.objects.values(
            'sku_id'
        ).distinct().annotate(
            value=Avg('number_of_outlet')
        ).values(
            'value',
            'sku_name',
        ).unarchived()


class BulkDeleteDistributionSnapUseCase(usecases.CreateUseCase):
    def _factory(self):
        SnapDistribution.objects.filter(
            is_archived=False,
            id__in=self._data.get('snap_ids')
        ).archive()


class ExportDistributionSnapUseCase(usecases.BaseUseCase):
    def __init__(self, filter_backends, request, view_self):
        self._view_self = view_self
        self._request = request
        self._filter_backends = filter_backends

    columns = [
        'Date', 'Country', 'City', 'Channel', 'Category', 'Brand', 'SKU',
        'Total Distribution', 'Shelf Share', 'Number Of Outlet'
    ]

    def _factory(self):
        response = HttpResponse(content_type='text/csv')
        filename = 'distribution_snap_snap.csv'
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

        # 1. write headers
        writer = csv.writer(response)
        writer.writerow(self.columns)

        # 2. write questions
        queryset = SnapDistribution.objects.unarchived().values(
            'date', 'country_name', 'city_name',
            'channel_name', 'category_name',
            'brand_name', 'sku_name',
            'total_distribution', 'shelf_share', 'number_of_outlet'
        )
        snaps = None
        for backend in list(self._filter_backends):
            snaps = backend().filter_queryset(self._request, queryset, self._view_self)

        for snap in snaps:
            writer.writerow([
                *snap.values()
            ])
        return response
