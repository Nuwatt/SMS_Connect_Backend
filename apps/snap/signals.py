from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.snap.models import SnapCity, PriceMonitorSnap, OutOfStockSnap, ConsumerSnap, DistributionSnap


@receiver(post_save, sender=SnapCity)
def archive_price_monitor_snap(sender, instance, **kwargs):
    if instance.is_archived:
        PriceMonitorSnap.objects.filter(snap_city=instance).update(is_archived=True)


@receiver(post_save, sender=SnapCity)
def archive_out_of_stock_snap(instance, **kwargs):
    if instance.is_archived:
        OutOfStockSnap.objects.filter(snap_city=instance).update(is_archived=True)


@receiver(post_save, sender=SnapCity)
def archive_consumer_snap(sender, instance, **kwargs):
    if instance.is_archived:
        ConsumerSnap.objects.filter(snap_city=instance).update(is_archived=True)


@receiver(post_save, sender=SnapCity)
def archive_distribution_snap(sender, instance, **kwargs):
    if instance.is_archived:
        DistributionSnap.objects.filter(snap_city=instance).update(is_archived=True)
