from django.urls import path

from apps.user.views import role_views

urlpatterns = [
    path(
        'list',
        role_views.ListRoleView.as_view(),
        name='list-role'
    ),
    path(
        'add',
        role_views.AddRoleView.as_view(),
        name='add-role'
    ),
]
