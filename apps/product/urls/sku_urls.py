from django.urls import path

from apps.product.views import sku_views

urlpatterns = [
    path(
        'add',
        sku_views.AddSKUView.as_view(),
        name='add-sku'

    ),
    path(
        'list',
        sku_views.ListSKUView.as_view(),
        name='list-sku'

    ),
    path(
        '<str:sku_id>/update',
        sku_views.UpdateSKUView.as_view(),
        name='update-sku'

    ),
    path(
        '<str:sku_id>/delete',
        sku_views.DeleteSKUView.as_view(),
        name='delete-sku'

    )
]
