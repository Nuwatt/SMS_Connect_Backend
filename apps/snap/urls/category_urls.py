from django.urls import path

from apps.snap.views import category_views

urlpatterns = [
    path(
        'add',
        category_views.AddSnapCategoryView.as_view(),
        name='add-snap-category'

    ),
    path(
        'list',
        category_views.ListSnapCategoryView.as_view(),
        name='list-snap-category'

    ),
    path(
        '<str:snap_category_id>/update',
        category_views.UpdateSnapCategoryView.as_view(),
        name='update-snap-category'

    ),
    path(
        '<str:snap_category_id>/delete',
        category_views.DeleteSnapCategoryView.as_view(),
        name='delete-snap-category'

    )
]
