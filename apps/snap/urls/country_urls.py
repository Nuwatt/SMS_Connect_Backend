from django.urls import path

from apps.snap.views import country_views

urlpatterns = [
    path(
        'add',
        country_views.AddSnapCountryView.as_view(),
        name='add-snap-country'

    ),
    path(
        'list',
        country_views.ListSnapCountryView.as_view(),
        name='list-snap-country'

    ),
    path(
        '<str:snap_country_id>/update',
        country_views.UpdateSnapCountryView.as_view(),
        name='update-snap-country'

    ),
    path(
        '<str:snap_country_id>/delete',
        country_views.DeleteSnapCountryView.as_view(),
        name='delete-snap-country'

    )
]
