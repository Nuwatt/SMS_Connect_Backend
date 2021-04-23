from django.urls import path, include

urlpatterns = [
    path(
        'city/',
        include('apps.localize.urls.city_urls')
    ),
    path(
        'country/',
        include('apps.localize.urls.country_urls')
    ),
    path(
        'area/',
        include('apps.localize.urls.area_urls')
    ),
    path(
        'nationality/',
        include('apps.localize.urls.nationality_urls')
    )
]
