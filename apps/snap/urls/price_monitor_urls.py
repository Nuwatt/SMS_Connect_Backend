from django.urls import path, include

from apps.snap.views import price_monitor_views

report_urls = [
    path(
        'overview',
        price_monitor_views.OverviewPriceMonitorSnapReportView.as_view(),
        name='overview-price-monitor-snap-report'
    ),
    path(
        'month-max',
        price_monitor_views.MonthMaxPriceMonitorSnapReportView.as_view(),
        name='month-max-price-monitor-snap-report'
    ),
    path(
        'month-min',
        price_monitor_views.MonthMaxPriceMonitorSnapReportView.as_view(),
        name='month-min-price-monitor-snap-report'
    ),
    path(
        'month-mode',
        price_monitor_views.MonthModePriceMonitorSnapReportView.as_view(),
        name='month-mode-price-monitor-snap-report'
    ),
    path(
        'month-mean',
        price_monitor_views.MonthMeanPriceMonitorSnapReportView.as_view(),
        name='month-mean-price-monitor-snap-report'
    ),
    path(
        'brand-overview',
        price_monitor_views.BrandOverviewPriceMonitorSnapReportView.as_view(),
        name='brand-overview-price-monitor-snap-report'
    )
]

urlpatterns = [
    path(
        'import',
        price_monitor_views.ImportPriceMonitorSnapView.as_view(),
        name='import-price-monitor-snap'
    ),
    path(
        'list',
        price_monitor_views.ListPriceMonitorSnapView.as_view(),
        name='list-price-monitor-snap'
    ),
    path(
        '<str:price_monitor_snap_id>/update',
        price_monitor_views.UpdatePriceMonitorSnapView.as_view(),
        name='update-price-monitor-snap'
    ),
    path(
        '<str:price_monitor_snap_id>/delete',
        price_monitor_views.DeletePriceMonitorSnapView.as_view(),
        name='delete-price-monitor-snap'
    ),
    path(
        'report/',
        include(report_urls)
    )
]
