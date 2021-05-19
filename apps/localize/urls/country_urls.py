from django.urls import path

from apps.localize.views import country_views

urlpatterns = [
    path(
        'add',
        country_views.AddCountryView.as_view(),
        name='add-country'

    ),
    path(
        'list',
        country_views.ListCountryView.as_view(),
        name='list-country'

    ),
    path(
        'nationality/list',
        country_views.ListNationalityView.as_view(),
        name='list-nationality'

    ),
    path(
        '<str:country_id>/update',
        country_views.UpdateCountryView.as_view(),
        name='update-country'

    ),
    path(
        '<str:country_id>/delete',
        country_views.DeleteCountryView.as_view(),
        name='delete-country'

    )
]
