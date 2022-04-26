from django.urls import path

from apps.snap.views import new_price_monitor_views

urlpatterns = [
    path(
        'city-max',
        new_price_monitor_views.CityMaxPriceMonitorSnapReportView.as_view(),
        name='city-max-price-monitor-snap-report'
    ),
]
