from django.urls import path

from apps.user import views

urlpatterns = [
    path(
        'signup',
        views.UserSignupView.as_view(),
        name='user-signup'
    ),
    path(
        'login',
        views.UserLoginView.as_view(),
        name='user-login'
    ),
    path(
        'list',
        views.ListUserView.as_view(),
        name='list-user'
    ),

]
