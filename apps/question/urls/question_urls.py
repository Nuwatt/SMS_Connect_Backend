from django.urls import path

from apps.question.views import question_views

urlpatterns = [
    path(
        'add',
        question_views.AddQuestionView.as_view(),
        name='add-question'
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
