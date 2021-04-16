from django.db import models

from apps.product import validators
from apps.core.models import BaseModel


class Category(BaseModel):
    """
    Category Model
    """
    name = models.CharField(
        max_length=224,
        validators=[validators.validate_category_name]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Brand(BaseModel):
    """
    Category Model
    """
    name = models.CharField(
        max_length=224,
        validators=[validators.validate_brand_name]
    )

    def __str__(self):
        return self.name


class SKU(BaseModel):
    """
    SKU Model
    """
    name = models.CharField(
        max_length=224,
        validators=[validators.validate_sku_name]
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
