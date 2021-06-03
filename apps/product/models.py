from django.db import models

from apps.core.models import BaseModel
from apps.core.utils import generate_custom_id


class Category(BaseModel):
    """
    Category Model
    """
    id = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        editable=False
    )

    name = models.CharField(
        max_length=224,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = generate_custom_id(initial='CA', model=Category)
        super(Category, self).save(*args, **kwargs)


class Brand(BaseModel):
    """
    Category Model
    """
    id = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        editable=False
    )

    name = models.CharField(
        max_length=224,
        unique=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = generate_custom_id(initial='BR', model=Brand)
        super(Brand, self).save(*args, **kwargs)


class SKU(BaseModel):
    """
    SKU Model
    """
    id = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        editable=False
    )

    name = models.CharField(
        max_length=224,
    )
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = generate_custom_id(initial='SKU', model=SKU)
        super(SKU, self).save(*args, **kwargs)
