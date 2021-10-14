from django.urls import path

from apps.snap.views import sku_views

urlpatterns = [
    path(
        'add',
        sku_views.AddSnapSKUView.as_view(),
        name='add-snap-sku'

    ),
    path(
        'list',
        sku_views.ListSnapSKUView.as_view(),
        name='list-snap-sku'

    ),
    path(
        '<str:snap_sku_id>/update',
        sku_views.UpdateSnapSKUView.as_view(),
        name='update-snap-sku'

    ),
    path(
        '<str:snap_sku_id>/delete',
        sku_views.DeleteSnapSKUView.as_view(),
        name='delete-snap-sku'

    )
]
