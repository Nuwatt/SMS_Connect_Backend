from django.urls import path, include

urlpatterns = [
    path(
        'price-monitor/',
        include('apps.report.urls.price_monitor_urls')
    ),
    path(
        'out-of-stock/',
        include('apps.report.urls.out_of_stock_urls')
    )
]
