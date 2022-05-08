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
    # city-report
    path(
        'city-report',
        out_of_stock_views.OutOfStockSnapCityReportView.as_view(),
        name='stock-snap-city-report'
    ),
    path(
        'not-available-by-week',
        out_of_stock_views.NotAvailableByWeekOutOfStockSnapReportView.as_view(),
        name='not-available-by-week-out-of-stock-snap-report'
    )
]

urlpatterns = [
    path(
        'import',
        out_of_stock_views.ImportOutOfStockSnapView.as_view(),
        name='import-out-of-stock-snap'
    ),
    path(
        'export',
        out_of_stock_views.ExportOutOfStockSnapView.as_view(),
        name='export-out-of-stock-snap'
    ),
    path(
        'list',
        out_of_stock_views.ListOutOfStockSnapView.as_view(),
        name='list-out-of-stock-snap'
    ),
    path(
        '<str:out_of_stock_snap_id>/update',
        out_of_stock_views.UpdateOutOfStockSnapView.as_view(),
        name='update-out-of-stock-snap'
    ),
    path(
        '<str:out_of_stock_snap_id>/delete',
        out_of_stock_views.DeleteOutOfStockSnapView.as_view(),
        name='delete-out-of-stock-snap'
    ),
    path(
        'bulk-delete',
        out_of_stock_views.BulkDeleteOutOfStockSnapView.as_view(),
        name='bulk-delete-out-of-stock-snap'
    ),
    path(
        'report/',
        include(report_urls)
    )
]
