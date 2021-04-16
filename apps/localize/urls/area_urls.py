from django.urls import path

from apps.localize.views import area_views

urlpatterns = [
    path(
        'add',
        area_views.AddAreaView.as_view(),
        name='add-area'

    ),
    path(
        'list',
        area_views.ListAreaView.as_view(),
        name='list-area'

    ),
    path(
        '<str:area_id>/update',
        area_views.UpdateAreaView.as_view(),
        name='update-area'

    ),
    path(
        '<str:area_id>/delete',
        area_views.DeleteAreaView.as_view(),
        name='delete-area'

    )
]
