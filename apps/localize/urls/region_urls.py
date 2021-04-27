from django.urls import path

from apps.localize.views import region_views

urlpatterns = [
    path(
        'add',
        region_views.AddRegionView.as_view(),
        name='add-region'

    ),
    path(
        'list',
        region_views.ListRegionView.as_view(),
        name='list-region'

    ),
    path(
        '<str:region_id>/update',
        region_views.UpdateRegionView.as_view(),
        name='update-region'

    ),
    path(
        '<str:area_id>/delete',
        region_views.DeleteRegionView.as_view(),
        name='delete-region'

    )
]
