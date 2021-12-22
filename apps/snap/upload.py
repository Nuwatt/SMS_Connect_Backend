import csv
from datetime import datetime

from apps.localize.models import Country, City
from apps.snap.models import (
    SnapChannel,
    SnapCategory,
    SnapBrand,
    SnapSKU,
    PriceMonitorSnap,
    SnapRetailer,
    SnapStore,
    OutOfStockSnap
)


def import_snap_pm():
    file = open('/home/xzibit/Documents/sms/Jeddah_2018.csv', 'r')
    csv_reader = csv.DictReader(file)
    item_list = list(csv_reader)

    country_data = {}
    city_data = {}
    channel_data = {}
    category_data = {}
    brand_data = {}
    sku_data = {}

    for item in item_list:
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
        print(snap.pk)


def import_snap_oos():
    file = open('/home/xzibit/Documents/sms/OOS1-2018.csv', 'r')
    csv_reader = csv.DictReader(file)
    item_list = list(csv_reader)

    country_data = {}
    city_data = {}
    channel_data = {}
    retailer_data = {}
    store_data = {}
    category_data = {}
    brand_data = {}
    sku_data = {}

    for item in item_list:
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
            sku.country.add(country_data[item.get('Country')])
            sku_data[item.get('SKU')] = sku

        snap, _snap_created = OutOfStockSnap.objects.update_or_create(
            city=city_data[item.get('City')],
            store=store_data[item.get('Store')],
            sku=sku_data[item.get('SKU')],
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
        print(snap.pk)
