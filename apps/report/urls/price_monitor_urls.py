from django.urls import path, include

from apps.report.views import price_monitor_views

urlpatterns = [
    path(
        'min-max',
        price_monitor_views.SKUMinMaxReportView.as_view(),
        name='sku-min-max-report'
    )
]
