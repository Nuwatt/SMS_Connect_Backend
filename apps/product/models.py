from django.db import models

from apps.core.models import BaseModel


class Category(BaseModel):
    """
    Category Model
    """
    name = models.CharField(
        max_length=224,
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
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name


class SKU(BaseModel):
    """
    SKU Model
    """
    name = models.CharField(
        max_length=224,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
