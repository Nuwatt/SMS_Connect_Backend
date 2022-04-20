from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel
from apps.core.utils import generate_custom_id
from apps.localize.models import City, Country
from apps.question.models import QuestionType


# ------Snap Localize ---------
class SnapCountry(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def clean(self):
        # check for unique name for unarchived list
        if SnapCountry.objects.filter(name__iexact=self.name, is_archived=False).exists():
            raise DjangoValidationError({
                'name': _('Country name already exists.')
            })


class SnapCity(BaseModel):
    country = models.ForeignKey(SnapCountry, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def clean(self):
        # check for unique name for unarchived list
        if SnapCity.objects.filter(name__iexact=self.name, is_archived=False, country=self.country).exists():
            raise DjangoValidationError({
                'name': _('Country name already exists.')
            })


# -----Snap Product-------
class SnapCategory(BaseModel):
    """
    Category Model
    """
    # id = models.CharField(
    #     max_length=50,
    #     unique=True,
    #     primary_key=True,
    #     editable=False
    # )

    name = models.CharField(max_length=224)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Snap Category'
        verbose_name_plural = 'Snap Categories'

    def clean(self):
        # check for unique name for unarchived list
        if SnapCategory.objects.filter(name__iexact=self.name, is_archived=False).exists():
            raise DjangoValidationError({
                'name': _('Category name already exists.')
            })

    # def save(self, *args, **kwargs):
    #     if self._state.adding:
    #         self.id = generate_custom_id(initial='CA', model=SnapCategory)
    #     super(SnapCategory, self).save(*args, **kwargs)


class SnapBrand(BaseModel):
    """
    Category Model
    """
    # id = models.CharField(
    #     max_length=50,
    #     unique=True,
    #     primary_key=True,
    #     editable=False
    # )

    name = models.CharField(max_length=224)

    def __str__(self):
        return self.name

    def clean(self):
        # check for unique name for unarchived list
        if SnapBrand.objects.filter(name__iexact=self.name, is_archived=False).exists():
            raise DjangoValidationError({
                'name': _('Brand name already exists.')
            })

    # def save(self, *args, **kwargs):
    #     if self._state.adding:
    #         self.id = generate_custom_id(initial='BR', model=SnapBrand)
    #     super(SnapBrand, self).save(*args, **kwargs)


class SnapSKU(BaseModel):
    """
    SKU Model
    """
    # id = models.CharField(
    #     max_length=50,
    #     unique=True,
    #     primary_key=True,
    #     editable=False
    # )

    name = models.CharField(max_length=224)
    brand = models.ForeignKey(SnapBrand, on_delete=models.CASCADE)
    category = models.ForeignKey(
        SnapCategory,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if self._state.adding:
    #         self.id = generate_custom_id(initial='SKU', model=SnapSKU)
    #     super(SnapSKU, self).save(*args, **kwargs)

    def clean(self):
        # check for unique name for unarchived list
        if SnapSKU.objects.filter(name__iexact=self.name, is_archived=False).exists():
            raise DjangoValidationError({
                'name': _('SKU name already exists.')
            })


# -----Snap Market-------------
class SnapChannel(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def clean(self):
        # check for unique name for unarchived list
        if SnapChannel.objects.filter(name__iexact=self.name, is_archived=False).exists():
            raise DjangoValidationError({
                'name': _('Channel name already exists.')
            })


class SnapRetailer(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def clean(self):
        # check for unique name for unarchived list
        if SnapRetailer.objects.filter(name__iexact=self.name, is_archived=False).exists():
            raise DjangoValidationError({
                'name': _('Retailer name already exists.')
            })


class SnapStore(BaseModel):
    name = models.CharField(max_length=100)
    retailer = models.ForeignKey(SnapRetailer, on_delete=models.CASCADE)
    channel = models.ForeignKey(
        SnapChannel,
        on_delete=models.CASCADE,
        null=True
    )

    city = models.ForeignKey(
        City,
        null=True,
        on_delete=models.CASCADE
    )
    snap_city = models.ForeignKey(
        SnapCity,
        null=True,
        on_delete=models.CASCADE
    )

    def clean(self):
        # check for unique name for unarchived list
        if SnapStore.objects.filter(name__iexact=self.name, is_archived=False).exists():
            raise DjangoValidationError({
                'name': _('Store name already exists.')
            })

    def __str__(self):
        return self.name


class PriceMonitorSnap(BaseModel):
    date = models.DateField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    snap_city = models.ForeignKey(
        SnapCity,
        null=True,
        on_delete=models.CASCADE
    )
    channel = models.ForeignKey(SnapChannel, null=True, on_delete=models.CASCADE)
    sku = models.ForeignKey(SnapSKU, null=True, on_delete=models.CASCADE)
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
    snap_city = models.ForeignKey(
        SnapCity,
        null=True,
        on_delete=models.CASCADE
    )
    store = models.ForeignKey(SnapStore, null=True, on_delete=models.CASCADE)
    sku = models.ForeignKey(SnapSKU, null=True, on_delete=models.CASCADE)
    count = models.IntegerField()
    not_available_in_month = models.FloatField()
    less_available_in_month = models.FloatField()
    available_in_month = models.FloatField()
    # store
    not_available_by_store = models.FloatField()
    less_available_by_store = models.FloatField()
    available_by_store = models.FloatField()
    # snap_city
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
    snap_city = models.ForeignKey(
        SnapCity,
        null=True,
        on_delete=models.CASCADE
    )
    channel = models.ForeignKey(SnapChannel, null=True, on_delete=models.CASCADE)
    sku = models.ForeignKey(SnapSKU, null=True, on_delete=models.CASCADE)
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
    snap_city = models.ForeignKey(
        SnapCity,
        null=True,
        on_delete=models.CASCADE
    )
    channel = models.ForeignKey(SnapChannel, null=True, on_delete=models.CASCADE)
    sku = models.ForeignKey(SnapSKU, null=True, on_delete=models.CASCADE)
    total_distribution = models.FloatField(blank=True, null=True)
    shelf_share = models.FloatField(blank=True, null=True)
    number_of_outlet = models.FloatField(blank=True, null=True)

    def __str__(self):
        return '{}-Distribution-Snap'.format(
            self.date.strftime('%Y-%m-%d')
        )


# new models
class SnapPriceMonitor(BaseModel):
    date = models.DateField(db_index=True)
    city_id = models.BigIntegerField(db_index=True)
    city_name = models.CharField(max_length=255, db_index=True)
    country_id = models.BigIntegerField(db_index=True)
    country_name = models.CharField(max_length=255, db_index=True)
    channel_id = models.BigIntegerField(db_index=True)
    channel_name = models.CharField(max_length=255, db_index=True)
    category_id = models.BigIntegerField(db_index=True)
    category_name = models.CharField(max_length=255, db_index=True)
    brand_id = models.BigIntegerField(db_index=True)
    brand_name = models.CharField(max_length=255, db_index=True)
    sku_id = models.BigIntegerField(db_index=True)
    sku_name = models.CharField(max_length=255, db_index=True)
    count = models.IntegerField()
    mode = models.FloatField()
    mean = models.FloatField()
    max = models.FloatField()
    min = models.FloatField()

    def __str__(self):
        return '{}-Price-Monitor'.format(
            self.date.strftime('%Y-%m-%d')
        )
