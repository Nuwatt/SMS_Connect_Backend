from django.urls import path, include

from apps.report.views import base_views

urlpatterns = [
    path(
        'price-monitor/',
        include('apps.report.urls.price_monitor_urls')
    ),
    path(
        'out-of-stock/',
        include('apps.report.urls.out_of_stock_urls')
    ),
    path(
        'overview',
        base_views.OverviewReportView.as_view(),
        name='overview-report'
    )
]
