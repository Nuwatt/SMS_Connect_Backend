from django.urls import path

from apps.market.views import retailer_views

urlpatterns = [
    path(
        'add',
        retailer_views.AddRetailerView.as_view(),
        name='add-retailer'
    ),
    path(
        'list',
        retailer_views.ListRetailerView.as_view(),
        name='list-retailer'
    ),
    path(
        'basic-list',
        retailer_views.BasicListRetailerView.as_view(),
        name='basic-list-retailer'
    ),
    path(
        '<str:retailer_id>/update',
        retailer_views.UpdateRetailerView.as_view(),
        name='update-retailer'
    ),
    path(
        '<str:retailer_id>/delete',
        retailer_views.DeleteRetailerView.as_view(),
        name='delete-retailer'
    ),
    path(
        'import',
        retailer_views.ImportRetailerView.as_view(),
        name='import-retailer'
    )
]
