from django.urls import path, include

urlpatterns = [
    path(
        'price-monitor/',
        include('apps.snap.urls.price_monitor_urls')
    )
]