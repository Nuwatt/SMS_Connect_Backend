from django.urls import path, include

from apps.user.views import portal_user_views

portal_user_urls = [
    path(
        'detail',
        portal_user_views.PortalUserDetailView.as_view(),
        name='portal-user-detail'
    ),
    path(
        'update',
        portal_user_views.UpdatePortalUserView.as_view(),
        name='update-portal-user'
    ),
    path(
        'delete',
        portal_user_views.DeletePortalUserView.as_view(),
        name='delete-portal-user'
    ),
    path(
        'avatar/upload',
        portal_user_views.UploadPortalUserAvatarView.as_view(),
        name='upload-portal-user-avatar'
    ),
]

urlpatterns = [
    path(
        'login',
        portal_user_views.PortalUserLoginView.as_view(),
        name='portal-login'
    ),
    path(
        'list',
        portal_user_views.ListPortalUserView.as_view(),
        name='list-portal-user'
    ),
    path(
        'register',
        portal_user_views.RegisterPortalUserView.as_view(),
        name='register-portal-user'
    ),
    path(
        '<str:portal_user_id>/',
        include(portal_user_urls)
    ),
]
