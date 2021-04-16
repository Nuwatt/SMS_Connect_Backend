from django.urls import path

from apps.product.views import brand_views

urlpatterns = [
    path(
        'add',
        brand_views.AddBrandView.as_view(),
        name='add-brand'

    ),
    path(
        'list',
        brand_views.ListBrandView.as_view(),
        name='list-brand'

    ),
    path(
        '<str:brand_id>/update',
        brand_views.UpdateBrandView.as_view(),
        name='update-brand'

    ),
    path(
        '<str:brand_id>/delete',
        brand_views.DeleteBrandView.as_view(),
        name='delete-brand'

    )
]
