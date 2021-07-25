from django.urls import path, include

# This file will contain all the end-points
urlpatterns = [
    path(
        'question/',
        include('apps.question.urls.base_urls')
    ),
    path(
        'user/',
        include('apps.user.urls.base_urls')
    ),
    path(
        'localize/',
        include('apps.localize.urls.base_urls')
    ),
    path(
        'product/',
        include('apps.product.urls.base_urls')
    ),
    path(
        'market/',
        include('apps.market.urls.base_urls')
    ),
    path(
        'questionnaire/',
        include('apps.questionnaire.urls.base_urls')
    ),
    path(
        'terms-and-conditions/',
        include('apps.terms_and_conditions.urls')
    ),
    path(
        'response/',
        include('apps.response.urls')
    ),
    path(
        'report/',
        include('apps.report.urls.base_urls')
    ), path(
        'snap/',
        include('apps.snap.urls.base_urls')
    )
]
