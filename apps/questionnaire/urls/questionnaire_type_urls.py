from django.urls import path

from apps.questionnaire.views import questionnaire_type_views

urlpatterns = [
    path(
        'add',
        questionnaire_type_views.AddQuestionnaireTypeView.as_view(),
        name='add-questionnaire-type'

    ),
    path(
        'list',
        questionnaire_type_views.ListQuestionnaireTypeView.as_view(),
        name='list-questionnaire-type'

    ),
    path(
        '<str:questionnaire_type_id>/update',
        questionnaire_type_views.UpdateQuestionnaireTypeView.as_view(),
        name='update-questionnaire-type'

    ),
    path(
        '<str:questionnaire_type_id>/delete',
        questionnaire_type_views.DeleteQuestionnaireTypeView.as_view(),
        name='delete-questionnaire-type'

    )
]
