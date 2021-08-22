from django.urls import path

from apps.snap.views import retailer_views

urlpatterns = [
    path(
        'add',
        retailer_views.AddSnapRetailerView.as_view(),
        name='add-snap-retailer'
    ),
    path(
        'list',
        retailer_views.ListSnapRetailerView.as_view(),
        name='list-snap-retailer'
    ),
    path(
        'basic-list',
        retailer_views.BasicListSnapRetailerView.as_view(),
        name='basic-list-snap-retailer'
    ),
    path(
        '<str:snap_retailer_id>/update',
        retailer_views.UpdateSnapRetailerView.as_view(),
        name='update-snap-retailer'
    ),
    path(
        '<str:snap_retailer_id>/delete',
        retailer_views.DeleteSnapRetailerView.as_view(),
        name='delete-snap-retailer'
    )
]
