from django.urls import path

from apps.user.views import agent_user_views

urlpatterns = [
    path(
        'list',
        agent_user_views.ListAgentUserView.as_view(),
        name='list-agent-user'
    ),
]
