from django.urls import path

from apps.user.views import portal_user_views

urlpatterns = [
    path(
        'list',
        portal_user_views.ListPortalUserView.as_view(),
        name='list-portal-user'
    ),
]
