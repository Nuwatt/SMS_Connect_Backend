from django.urls import path, include

urlpatterns = [
    path(
        '',
        include('apps.question.urls.question_urls')
    )
]
