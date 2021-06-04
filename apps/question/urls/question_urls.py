from django.urls import path

from apps.question.views import question_views

urlpatterns = [
    path(
        'questionnaire/<str:questionnaire_id>/add',
        question_views.AddQuestionView.as_view(),
        name='add-question'
    ),
    path(
        'questionnaire/<str:questionnaire_id>/bulk-add',
        question_views.BulkAddQuestionView.as_view(),
        name='bulk-add-question'
    ),
    path(
        'questionnaire/<str:questionnaire_id>/list',
        question_views.ListQuestionForAgentView.as_view(),
        name='list-question-for-agent-user'
    ),
    path(
        'questionnaire/<str:questionnaire_id>/import',
        question_views.ImportQuestionView.as_view(),
        name='import-question'
    ),
    path(
        'questionnaire/<str:questionnaire_id>/export',
        question_views.ExportQuestionView.as_view(),
        name='export-question'
    ),
    path(
        'list',
        question_views.ListQuestionView.as_view(),
        name='list-questions'
    ),
    path(
        '<str:question_id>/detail',
        question_views.QuestionDetailView.as_view(),
        name='question-detail'
    )
]
