from django.urls import path, include

urlpatterns = [
    path(
        '',
        include('apps.questionnaire.urls.questionnaire_urls')
    ),
    path(
        'questionnaire-type/',
        include('apps.questionnaire.urls.questionnaire_type_urls')
    ),
]
