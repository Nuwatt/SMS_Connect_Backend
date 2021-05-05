from django.urls import path

from apps.questionnaire.views import questionnaire_views

urlpatterns = [
    path(
        'add',
        questionnaire_views.AddQuestionnaireView.as_view(),
        name='add-questionnaire'

    ),
    path(
        'list',
        questionnaire_views.ListQuestionnaireView.as_view(),
        name='list-questionnaire'

    ),
    path(
        '<str:questionnaire_id>/update',
        questionnaire_views.UpdateQuestionnaireView.as_view(),
        name='update-questionnaire'

    ),
    path(
        '<str:questionnaire_id>/delete',
        questionnaire_views.DeleteQuestionnaireView.as_view(),
        name='delete-questionnaire'

    ),
    path(
        '<str:questionnaire_id>/detail',
        questionnaire_views.QuestionnaireDetailView.as_view(),
        name='questionnaire-detail'

    ),
    path(
        'available-for-agent',
        questionnaire_views.ListAvailableQuestionnaireForAgentView.as_view(),
        name='list-available-questionnaire-for-agent'

    )
]
