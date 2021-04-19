from django.urls import path, include

urlpatterns = [
    path(
        '',
        include('apps.question.urls.question_urls')
    ),
    path(
        'question-type/',
        include('apps.question.urls.question_type_urls')
    )
]
