from django.urls import path

from apps.response import views

urlpatterns = [
    path(
        'questionnaire/<str:questionnaire_id>/start',
        views.StartQuestionnaireView.as_view(),
        name='start-questionnaire'
    ),
]
