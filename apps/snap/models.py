from django.db import models

from apps.core.models import BaseModel
from apps.localize.models import City
from apps.market.models import Channel
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

