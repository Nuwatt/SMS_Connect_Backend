from django.urls import path, include

urlpatterns = [
    path(
        'price-monitor/',
        include('apps.report.urls.price_monitor_urls')
    )
]
