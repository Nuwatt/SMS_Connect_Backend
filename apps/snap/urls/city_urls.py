from django.urls import path

from apps.snap.views import city_views

urlpatterns = [
    path(
        'add',
        city_views.AddSnapCityView.as_view(),
        name='add-snap-snap_city'

    ),
    path(
        'list',
        city_views.ListSnapCityView.as_view(),
        name='list-snap-snap_city'

    ),
    path(
        '<str:snap_city_id>/update',
        city_views.UpdateSnapCityView.as_view(),
        name='update-snap-snap_city'

    ),
    path(
        '<str:snap_city_id>/delete',
        city_views.DeleteSnapCityView.as_view(),
        name='delete-snap-snap_city'

    )
]
