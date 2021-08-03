from django.urls import path, include

from apps.snap.views import out_of_stock_views

report_urls = [
    path(
        'overview',
        out_of_stock_views.OverviewPriceMonitorSnapReportView.as_view(),
        name='overview-out-of-stock-snap-report'
    ),
    path(
        'available',
        out_of_stock_views.AvailableOutOfStockSnapReportView.as_view(),
        name='available-out-of-stock-snap-report'
    ),
    path(
        'not-available',
        out_of_stock_views.NotAvailableOutOfStockSnapReportView.as_view(),
        name='not-available-out-of-stock-snap-report'
    ),
    path(
        'less',
        out_of_stock_views.LessOutOfStockSnapReportView.as_view(),
        name='less-out-of-stock-snap-report'
    ),
    # city
    path(
        'available-by-city',
        out_of_stock_views.AvailableByCityOutOfStockSnapReportView.as_view(),
        name='available-by-city-out-of-stock-snap-report'
    ),
    path(
        'not-available-by-city',
        out_of_stock_views.NotAvailableByCityOutOfStockSnapReportView.as_view(),
        name='not-available-by-city-out-of-stock-snap-report'
    ),
    path(
        'less-by-city',
        out_of_stock_views.LessByCityOutOfStockSnapReportView.as_view(),
        name='less-by-city-out-of-stock-snap-report'
    ),
    path(
        'visit-by-city',
        out_of_stock_views.VisitByCityOutOfStockSnapReportView.as_view(),
        name='visit-by-city-out-of-stock-snap-report'
    ),
#     path(
#         'month-min',
#         price_monitor_views.MonthMaxPriceMonitorSnapReportView.as_view(),
#         name='month-min-price-monitor-snap-report'
#     ),
#     path(
#         'month-mode',
#         price_monitor_views.MonthModePriceMonitorSnapReportView.as_view(),
#         name='month-mode-price-monitor-snap-report'
#     ),
#     path(
#         'month-mean',
#         price_monitor_views.MonthMeanPriceMonitorSnapReportView.as_view(),
#         name='month-mean-price-monitor-snap-report'
#     ),
#     path(
#         'brand-overview',
#         price_monitor_views.BrandOverviewPriceMonitorSnapReportView.as_view(),
#         name='brand-overview-price-monitor-snap-report'
#     ),
#     path(
#         'country-min',
#         price_monitor_views.CountryMinPriceMonitorSnapReportView.as_view(),
#         name='country-min-price-monitor-snap-report'
#     ),
#     path(
#         'country-max',
#         price_monitor_views.CountryMaxPriceMonitorSnapReportView.as_view(),
#         name='country-max-price-monitor-snap-report'
#     ),
#     path(
#         'country-mean',
#         price_monitor_views.CountryMeanPriceMonitorSnapReportView.as_view(),
#         name='country-mean-price-monitor-snap-report'
#     ),
#     path(
#         'country-mode',
#         price_monitor_views.CountryModePriceMonitorSnapReportView.as_view(),
#         name='country-mode-price-monitor-snap-report'
#     ),
#     path(
#         'visit-per-city',
#         price_monitor_views.VisitPerCityPriceMonitorSnapReportView.as_view(),
#         name='visit-per-city-price-monitor-snap-report'
#     ),
#     path(
#         'visit-per-country',
#         price_monitor_views.VisitPerCountryPriceMonitorSnapReportView.as_view(),
#         name='visit-per-country-price-monitor-snap-report'
#     ),
#     path(
#         'sku-per-channel',
#         price_monitor_views.SKUPerChannelPriceMonitorSnapReportView.as_view(),
#         name='sku-per-channel-price-monitor-snap-report'
#     )
]

urlpatterns = [
    path(
        'import',
        out_of_stock_views.ImportOutOfStockSnapView.as_view(),
        name='import-out-of-stock-snap'
    ),
    path(
        'list',
        out_of_stock_views.ListOutOfStockSnapView.as_view(),
        name='list-out-of-stock-snap'
    ),
    path(
        '<str:price_monitor_snap_id>/update',
        out_of_stock_views.UpdateOutOfStockSnapView.as_view(),
        name='update-out-of-stock-snap'
    ),
    path(
        '<str:price_monitor_snap_id>/delete',
        out_of_stock_views.DeleteOutOfStockSnapView.as_view(),
        name='delete-out-of-stock-snap'
    ),
    path(
        'report/',
        include(report_urls)
    )
]
