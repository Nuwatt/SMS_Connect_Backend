from django.db import models

from apps.core.models import BaseModel
from apps.localize.models import City
from apps.market.models import Channel, Store
from apps.product.models import SKU, Category, Brand


class PriceMonitorSnap(BaseModel):
    date = models.DateField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    count = models.IntegerField()
    mode = models.FloatField()
    mean = models.FloatField()
    max = models.FloatField()
    min = models.FloatField()

    def __str__(self):
        return '{}-Price-Monitor'.format(
            self.date.strftime('%Y-%m-%d')
        )


class OutOfStockSnap(BaseModel):
    date = models.DateField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    count = models.IntegerField()
    not_available_in_month = models.FloatField()
    less_available_in_month = models.FloatField()
    available_in_month = models.FloatField()
    # store
    not_available_by_store = models.FloatField()
    less_available_by_store = models.FloatField()
    available_by_store = models.FloatField()
    # city
    not_available_by_city = models.FloatField()
    less_available_by_city = models.FloatField()
    available_by_city = models.FloatField()

    def __str__(self):
        return '{}-Out-of-Monitor'.format(
            self.date.strftime('%Y-%m-%d')
        )
