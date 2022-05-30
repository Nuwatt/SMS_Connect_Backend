from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.snap import models


@receiver(post_save, sender=models.SnapCity)
def update_for_snap_city(sender, instance, **kwargs):
    # SnapPriceMonitor
    models.SnapPriceMonitor.objects.filter(city_id=instance.id).update(
        is_archived=instance.is_archived,
        city_name=instance.name
    )

    # SnapOutOfStock
    models.SnapOutOfStock.objects.filter(city_id=instance.id).update(
        is_archived=instance.is_archived,
        city_name=instance.name
    )

    # consumer
    models.SnapConsumer.objects.filter(city_id=instance.id).update(
        is_archived=instance.is_archived,
        city_name=instance.name
    )

    # distribution
    models.SnapDistribution.objects.filter(city_id=instance.id).update(
        is_archived=instance.is_archived,
        city_name=instance.name
    )


@receiver(post_save, sender=models.SnapCountry)
def update_for_snap_country(sender, instance, **kwargs):
    # SnapPriceMonitor
    models.SnapPriceMonitor.objects.filter(country_id=instance.id).update(
        is_archived=instance.is_archived,
        country_name=instance.name
    )

    # SnapOutOfStock
    models.SnapOutOfStock.objects.filter(country_id=instance.id).update(
        is_archived=instance.is_archived,
        country_name=instance.name
    )

    # consumer
    models.SnapConsumer.objects.filter(country_id=instance.id).update(
        is_archived=instance.is_archived,
        country_name=instance.name
    )

    # distribution
    models.SnapDistribution.objects.filter(country_id=instance.id).update(
        is_archived=instance.is_archived,
        country_name=instance.name
    )


@receiver(post_save, sender=models.SnapCategory)
def update_for_snap_category(sender, instance, **kwargs):
    # SnapPriceMonitor
    models.SnapPriceMonitor.objects.filter(category_id=instance.id).update(
        is_archived=instance.is_archived,
        category_name=instance.name
    )

    # SnapOutOfStock
    models.SnapOutOfStock.objects.filter(category_id=instance.id).update(
        is_archived=instance.is_archived,
        category_name=instance.name
    )

    # consumer
    models.SnapConsumer.objects.filter(category_id=instance.id).update(
        is_archived=instance.is_archived,
        category_name=instance.name
    )

    # distribution
    models.SnapDistribution.objects.filter(category_id=instance.id).update(
        is_archived=instance.is_archived,
        category_name=instance.name
    )


@receiver(post_save, sender=models.SnapBrand)
def update_for_snap_brand(sender, instance, **kwargs):
    # SnapPriceMonitor
    models.SnapPriceMonitor.objects.filter(brand_id=instance.id).update(
        is_archived=instance.is_archived,
        brand_name=instance.name
    )

    # SnapOutOfStock
    models.SnapOutOfStock.objects.filter(brand_id=instance.id).update(
        is_archived=instance.is_archived,
        brand_name=instance.name
    )

    # consumer
    models.SnapConsumer.objects.filter(brand_id=instance.id).update(
        is_archived=instance.is_archived,
        brand_name=instance.name
    )

    # distribution
    models.SnapDistribution.objects.filter(brand_id=instance.id).update(
        is_archived=instance.is_archived,
        brand_name=instance.name
    )


@receiver(post_save, sender=models.SnapSKU)
def update_for_snap_sku(sender, instance, **kwargs):
    # SnapPriceMonitor
    models.SnapPriceMonitor.objects.filter(sku_id=instance.id).update(
        is_archived=instance.is_archived,
        sku_name=instance.name
    )

    # SnapOutOfStock
    models.SnapOutOfStock.objects.filter(sku_id=instance.id).update(
        is_archived=instance.is_archived,
        sku_name=instance.name
    )

    # consumer
    models.SnapConsumer.objects.filter(sku_id=instance.id).update(
        is_archived=instance.is_archived,
        sku_name=instance.name
    )

    # distribution
    models.SnapDistribution.objects.filter(sku_id=instance.id).update(
        is_archived=instance.is_archived,
        sku_name=instance.name
    )


@receiver(post_save, sender=models.SnapChannel)
def update_for_snap_channel(sender, instance, **kwargs):
    # SnapPriceMonitor
    models.SnapPriceMonitor.objects.filter(channel_id=instance.id).update(
        is_archived=instance.is_archived,
        channel_name=instance.name
    )

    # SnapOutOfStock
    models.SnapOutOfStock.objects.filter(channel_id=instance.id).update(
        is_archived=instance.is_archived,
        channel_name=instance.name
    )

    # consumer
    models.SnapConsumer.objects.filter(channel_id=instance.id).update(
        is_archived=instance.is_archived,
        channel_name=instance.name
    )

    # distribution
    models.SnapDistribution.objects.filter(channel_id=instance.id).update(
        is_archived=instance.is_archived,
        channel_name=instance.name
    )


@receiver(post_save, sender=models.SnapRetailer)
def update_for_snap_retailer(sender, instance, **kwargs):
    # SnapOutOfStock
    models.SnapOutOfStock.objects.filter(retailer_id=instance.id).update(
        is_archived=instance.is_archived,
        retailer_name=instance.name
    )


@receiver(post_save, sender=models.SnapStore)
def update_for_snap_store(sender, instance, **kwargs):
    # SnapOutOfStock
    models.SnapOutOfStock.objects.filter(store_id=instance.id).update(
        is_archived=instance.is_archived,
        store_name=instance.name
    )
