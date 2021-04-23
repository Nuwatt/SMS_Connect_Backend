from django.urls import path

from apps.localize.views import nationality_views

urlpatterns = [
    path(
        'add',
        nationality_views.AddNationalityView.as_view(),
        name='add-nationality'

    ),
    path(
        'list',
        nationality_views.ListNationalityView.as_view(),
        name='list-nationality'

    ),
    path(
        '<str:nationality_id>/update',
        nationality_views.UpdateNationalityView.as_view(),
        name='update-nationality'

    ),
    path(
        '<str:nationality_id>/delete',
        nationality_views.DeleteNationalityView.as_view(),
        name='delete-nationality'

    )
]
