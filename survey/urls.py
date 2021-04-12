from django.urls import path
from survey.views import *

urlpatterns = [
    path('signup', UserSignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),

]
