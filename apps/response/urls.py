from django.urls import path

from apps.response import views

urlpatterns = [
    path(
        'questionnaire/<str:questionnaire_id>/start',
        views.StartQuestionnaireView.as_view(),
        name='start-questionnaire'
    ),
    path(
        '<str:response_id>/submit',
        views.SummitQuestionnaireResponseView.as_view(),
        name='submit-questionnaire-response'
    ),
    path(
        'agent-user/history',
        views.ListAgentResponseHistoryView.as_view(),
        name='list-agent-response-history'
    ),
    path(
        'agent-user/<str:agent_user_id>/list',
        views.ListAgentResponseView.as_view(),
        name='list-agent-response'
    ),
    path(
        'questionnaire/<str:questionnaire_id>/list',
        views.ListQuestionnaireResponseView.as_view(),
        name='list-questionnaire-response'
    ),
]
