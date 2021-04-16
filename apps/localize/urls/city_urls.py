from django.urls import path

from apps.localize.views import city_views

urlpatterns = [
    path(
        'add',
        city_views.AddCityView.as_view(),
        name='add-city'

    ),
    path(
        'list',
        city_views.ListCityView.as_view(),
        name='list-city'

    ),
    path(
        '<str:city_id>/update',
        city_views.UpdateCityView.as_view(),
        name='update-city'

    ),
    path(
        '<str:city_id>/delete',
        city_views.DeleteCityView.as_view(),
        name='delete-city'

    )
]
