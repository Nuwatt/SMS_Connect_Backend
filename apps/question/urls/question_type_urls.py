from django.urls import path

from apps.question.views import question_type_views

urlpatterns = [
    path(
        'add',
        question_type_views.AddQuestionView.as_view(),
        name='add-question-type'
    ),
    path(
        'list',
        question_type_views.ListQuestionView.as_view(),
        name='list-question-type'
    ),
    path(
        '<str:question_type_id>/detail',
        question_type_views.QuestionDetailView.as_view(),
        name='question-type-detail'
    )
]
