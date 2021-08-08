from django.db import models

from apps.core.models import BaseModel
from apps.localize.models import City
from apps.market.models import Channel, Store
from apps.product.models import SKU, Category, Brand
from apps.question.models import QuestionType


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


class ConsumerSnap(BaseModel):
    date = models.DateField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    count = models.IntegerField()
    question_statement = models.CharField(max_length=250)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    total_yes = models.FloatField(null=True, blank=True)
    total_no = models.FloatField(null=True, blank=True)
    # rating 1 to 3
    rating_one_on_three = models.FloatField(null=True, blank=True)
    rating_two_on_three = models.FloatField(null=True, blank=True)
    rating_three_on_three = models.FloatField(null=True, blank=True)
    # rating 1 to 5
    rating_one_on_five = models.FloatField(null=True, blank=True)
    rating_two_on_five = models.FloatField(null=True, blank=True)
    rating_three_on_five = models.FloatField(null=True, blank=True)
    rating_four_on_five = models.FloatField(null=True, blank=True)
    rating_five_on_five = models.FloatField(null=True, blank=True)
    # rating 1 to 10
    rating_one_on_ten = models.FloatField(null=True, blank=True)
    rating_two_on_ten = models.FloatField(null=True, blank=True)
    rating_three_on_ten = models.FloatField(null=True, blank=True)
    rating_four_on_ten = models.FloatField(null=True, blank=True)
    rating_five_on_ten = models.FloatField(null=True, blank=True)
    rating_six_on_ten = models.FloatField(null=True, blank=True)
    rating_seven_on_ten = models.FloatField(null=True, blank=True)
    rating_eight_on_ten = models.FloatField(null=True, blank=True)
    rating_nine_on_ten = models.FloatField(null=True, blank=True)
    rating_ten_on_ten = models.FloatField(null=True, blank=True)
    # average numeric
    average_numeric = models.FloatField(null=True, blank=True)

    def __str__(self):
        return '{}-Consumer-Snap'.format(
            self.date.strftime('%Y-%m-%d')
        )


class DistributionSnap(BaseModel):
    date = models.DateField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    count = models.IntegerField()
    sku_by_city = models.FloatField(blank=True, null=True)
    sku_by_country = models.FloatField(blank=True, null=True)
    sku_by_channel = models.FloatField(blank=True, null=True)
    brand_by_city = models.FloatField(blank=True, null=True)
    brand_by_country = models.FloatField(blank=True, null=True)
    share_brand_by_country = models.FloatField(blank=True, null=True)
    share_brand_by_channel = models.FloatField(blank=True, null=True)
    share_sku_by_channel = models.FloatField(blank=True, null=True)
    share_sku_by_country = models.FloatField(blank=True, null=True)

    def __str__(self):
        return '{}-Distribution-Snap'.format(
            self.date.strftime('%Y-%m-%d')
        )
