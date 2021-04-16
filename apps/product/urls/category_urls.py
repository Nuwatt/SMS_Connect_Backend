from django.urls import path

from apps.product.views import category_views

urlpatterns = [
    path(
        'add',
        category_views.AddCategoryView.as_view(),
        name='add-category'

    ),
    path(
        'list',
        category_views.ListCategoryView.as_view(),
        name='list-category'

    ),
    path(
        '<str:category_id>/update',
        category_views.UpdateCategoryView.as_view(),
        name='update-category'

    ),
    path(
        '<str:category_id>/delete',
        category_views.DeleteCategoryView.as_view(),
        name='delete-category'

    )
]
