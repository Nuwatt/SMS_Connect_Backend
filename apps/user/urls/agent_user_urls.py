from django.urls import path, include

from apps.user.views import agent_user_views

agent_user_urls = [
    path(
        'detail',
        agent_user_views.AgentUserDetailView.as_view(),
        name='portal-agent-detail'
    ),
    path(
        'update',
        agent_user_views.UpdateAgentUserView.as_view(),
        name='update-agent-user'
    ),
    path(
        'delete',
        agent_user_views.DeleteAgentUserView.as_view(),
        name='delete-agent-user'
    ),
    path(
        'avatar/upload',
        agent_user_views.UploadPortalUserAvatarView.as_view(),
        name='upload-agent-user-avatar'
    ),
]

urlpatterns = [
    path(
        'login',
        agent_user_views.AgentUserLoginView.as_view(),
        name='agent-login'
    ),
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
    path(
        '<str:agent_user_id>/',
        include(agent_user_urls)
    ),
]
