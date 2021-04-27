from django.urls import path

from apps.user.views import agent_user_views

urlpatterns = [
    path(
        'list',
        agent_user_views.ListAgentUserView.as_view(),
        name='list-agent-user'
    ),
    path(
        'register',
        agent_user_views.RegisterAgentUserView.as_view(),
        name='register-agent-user'
    ),
    path(
        'profile',
        agent_user_views.AgentUserProfileView.as_view(),
        name='agent-user-profile'
    ),
    path(
        'profile/update',
        agent_user_views.UpdateAgentUserProfileView.as_view(),
        name='update-agent-user-profile'
    ),
]
