from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.snap.models import SnapCity, SnapDistribution, SnapOutOfStock, SnapPriceMonitor, ConsumerSnap


@receiver(post_save, sender=SnapCity)
def archive_price_monitor_snap(sender, instance, **kwargs):
    if instance.is_archived:
        SnapPriceMonitor.objects.filter(snap_city=instance).update(is_archived=True)


@receiver(post_save, sender=SnapCity)
def archive_out_of_stock_snap(instance, **kwargs):
    if instance.is_archived:
        SnapOutOfStock.objects.filter(snap_city=instance).update(is_archived=True)


@receiver(post_save, sender=SnapCity)
def archive_consumer_snap(sender, instance, **kwargs):
    if instance.is_archived:
        ConsumerSnap.objects.filter(snap_city=instance).update(is_archived=True)


@receiver(post_save, sender=SnapCity)
def archive_distribution_snap(sender, instance, **kwargs):
    if instance.is_archived:
        SnapDistribution.objects.filter(snap_city=instance).update(is_archived=True)
