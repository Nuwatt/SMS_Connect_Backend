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
        'password/change',
        base_views.ChangePasswordView.as_view(),
        name='change-password'
    ),
    path(
        'password/reset',
        base_views.PasswordResetView.as_view(),
        name='password-reset'
    ),
    path(
        'password/reset/confirm',
        base_views.PasswordResetConfirmView.as_view(),
        name='password-reset-confirm'
    ),
    path(
        'support',
        base_views.SupportView.as_view(),
        name='support'
    ),
    path(
        'agent-user/',
        include('apps.user.urls.agent_user_urls')
    ),
    path(
        'portal-user/',
        include('apps.user.urls.portal_user_urls')
    ),
    path(
        'role/',
        include('apps.user.urls.role_urls')
    ),
]
