import csv
from datetime import datetime

from django.db import IntegrityError
from django.db.models import F, Sum
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.localize.models import Country, City
from apps.snap.exceptions import DistributionSnapNotFound
from apps.snap.models import DistributionSnap, SnapChannel, SnapRetailer, SnapStore, SnapCategory, SnapBrand, SnapSKU


class GetDistributionSnapUseCase(usecases.BaseUseCase):
    def __init__(self, distribution_snap_id: str):
        self._distribution_snap_id = distribution_snap_id

    def execute(self):
        self._factory()
        return self._distribution_snap

    def _factory(self):
        try:
            self._distribution_snap = DistributionSnap.objects.get(pk=self._distribution_snap_id)
        except DistributionSnap.DoesNotExist:
            raise DistributionSnapNotFound


class ImportDistributionSnapUseCase(usecases.ImportCSVUseCase):
    def __init__(self, serializer):
        super().__init__(serializer)

    valid_columns = [
        'Date', 'Country', 'City', 'Channel', 'Category', 'Brand', 'SKU', 'Count',
        'SKU By City', 'SKU By Channel'
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
                channel, _created = SnapChannel.objects.get_or_create(
                    name=item.get('Channel'),
                    is_archived=False
                )
                channel_data[item.get('Channel')] = channel

            if item.get('Category') not in category_data:
                category, _created = SnapCategory.objects.get_or_create(
                    name=item.get('Category'),
                    is_archived=False
                )
                category_data[item.get('Category')] = category

            if item.get('Brand') not in brand_data:
                brand, _created = SnapBrand.objects.get_or_create(
                    name=item.get('Brand'),
                    is_archived=False
                )
                brand_data[item.get('Brand')] = brand

            if item.get('SKU') not in sku_data:
                sku, _created = SnapSKU.objects.get_or_create(
                    name=item.get('SKU'),
                    brand=brand_data[item.get('Brand')],
                    category=category_data[item.get('Category')],
                    is_archived=False
                )
                sku.country.add(country_data[item.get('Country')])
                sku_data[item.get('SKU')] = sku

            snap, _created = DistributionSnap.objects.update_or_create(
                city=city_data[item.get('City')],
                channel=channel_data[item.get('Channel')],
                sku=sku_data[item.get('SKU')],
                date=datetime.strptime(item.get('Date'), "%Y-%m-%d").date(),
                defaults={
                    'count': item.get('Count'),
                    'sku_by_city': item.get('SKU By City'),
                    'sku_by_channel': item.get('SKU By Channel')
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
    def execute(self):
        return self._factory()

    def _factory(self):
        return DistributionSnap.objects.select_related(
            'city',
            'city__country',
            'sku__category',
            'sku__brand',
            'sku',
            'channel',
        ).unarchived()


class DeleteDistributionSnapUseCase(usecases.DeleteUseCase):
    def __init__(self, price_monitor_snap: DistributionSnap):
        super().__init__(price_monitor_snap)


class UpdateDistributionSnapUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, price_monitor_snap: DistributionSnap):
        super().__init__(serializer, price_monitor_snap)


class VisitByCountryDistributionSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return DistributionSnap.objects.values(
            'city__country'
        ).distinct().annotate(
            value=Sum('count'),
            country_name=F('city__country__name'),
        ).values(
            'country_name',
            'value'
        ).unarchived()


class VisitByCityDistributionSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return DistributionSnap.objects.values(
            'city'
        ).distinct().annotate(
            value=Sum('count'),
            city_name=F('city__name'),
        ).values(
            'city_name',
            'value'
        ).unarchived()


class VisitByChannelDistributionSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return DistributionSnap.objects.values(
            'store__channel'
        ).distinct().annotate(
            value=Sum('count'),
            channel_name=F('store__channel__name'),
        ).values(
            'channel_name',
            'value'
        ).unarchived()


class SKUByCityDistributionSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return DistributionSnap.objects.values(
            'city'
        ).distinct().annotate(
            value=Sum('sku_by_city'),
            city_name=F('city__name'),
            sku_name=F('sku__name'),
        ).values(
            'city_name',
            'sku_name',
            'value'
        ).unarchived()


class SKUByChannelDistributionSnapReportUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return DistributionSnap.objects.values(
            'store__channel'
        ).distinct().annotate(
            value=Sum('sku_by_channel'),
            channel_name=F('store__channel__name'),
            sku_name=F('sku__name'),
        ).values(
            'channel_name',
            'sku_name',
            'value'
        ).unarchived()


class BulkDeleteDistributionSnapUseCase(usecases.CreateUseCase):
    def _factory(self):
        DistributionSnap.objects.filter(
            is_archived=False,
            id__in=self._data.get('snap_ids')
        ).archive()


class ExportDistributionSnapUseCase(usecases.BaseUseCase):
    columns = [
        'Date', 'Country', 'City', 'Channel', 'Retailer', 'Store', 'Category', 'Brand', 'SKU', 'Count',
        'SKU By City', 'SKU By Country', 'SKU By Channel', 'Brand By City', 'Brand By Country',
        'Share Brand By Country', 'Share Brand By Channel', 'Share SKU By Channel', 'Share SKU By Country'
    ]

    def execute(self):
        return self._factory()

    def _factory(self):
        response = HttpResponse(content_type='text/csv')
        filename = 'distribution_snap_snap.csv'
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

        # 1. write headers
        writer = csv.writer(response)
        writer.writerow(self.columns)

        # 2. write questions
        snaps = DistributionSnap.objects.unarchived().values(
            'date', 'city__country__name', 'city__name', 'store__channel__name',
            'store__retailer__name', 'store__name', 'sku__category__name',
            'sku__brand__name', 'sku__name', 'count',
            'sku_by_city', 'sku_by_country', 'sku_by_channel', 'brand_by_city',
            'brand_by_country', 'share_brand_by_country', 'share_brand_by_channel',
            'share_sku_by_channel', 'share_sku_by_country'
        )
        for snap in snaps:
            writer.writerow([
                *snap.values()
            ])
        return response
