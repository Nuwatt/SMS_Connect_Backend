from django.urls import path, include

from apps.user.views import base_views

urlpatterns = [
    path(
        'signup',
        base_views.UserSignupView.as_view(),
        name='user-signup'
    ),
    path(
        'login',
        base_views.UserLoginView.as_view(),
        name='user-login'
    ),
    path(
        'agent-user/',
        include('apps.user.urls.agent_user_urls')
    ),
    path(
        'portal-user/',
        include('apps.user.urls.portal_user_urls')
    ),
]
