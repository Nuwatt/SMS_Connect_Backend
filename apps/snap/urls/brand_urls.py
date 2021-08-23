from django.urls import path

from apps.snap.views import brand_views

urlpatterns = [
    path(
        'add',
        brand_views.AddSnapBrandView.as_view(),
        name='add-snap-brand'

    ),
    path(
        'list',
        brand_views.ListSnapBrandView.as_view(),
        name='list-snap-brand'

    ),
    path(
        '<str:snap_brand_id>/update',
        brand_views.UpdateSnapBrandView.as_view(),
        name='update-snap-brand'

    ),
    path(
        '<str:snap_brand_id>/delete',
        brand_views.DeleteSnapBrandView.as_view(),
        name='delete-snap-brand'

    )
]
