from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel
from apps.core.utils import generate_custom_id
from apps.localize.models import Country


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

    name = models.CharField(max_length=224)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def clean(self):
        # check for unique name for unarchived list
        if Category.objects.filter(name__iexact=self.name, is_archived=False).exists():
            raise DjangoValidationError({
                'name': _('Category name already exists.')
            })

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

    name = models.CharField(max_length=224)

    def __str__(self):
        return self.name

    def clean(self):
        # check for unique name for unarchived list
        if Brand.objects.filter(name__iexact=self.name, is_archived=False).exists():
            raise DjangoValidationError({
                'name': _('Brand name already exists.')
            })

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

    name = models.CharField(max_length=224)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.CASCADE
    )
    country = models.ManyToManyField(Country, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = generate_custom_id(initial='SKU', model=SKU)
        super(SKU, self).save(*args, **kwargs)

    def clean(self):
        # check for unique name for unarchived list
        if SKU.objects.filter(name__iexact=self.name, is_archived=False).exists():
            raise DjangoValidationError({
                'name': _('SKU name already exists.')
            })
