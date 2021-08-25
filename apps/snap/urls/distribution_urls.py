from django.urls import path, include

from apps.snap.views import distribution_views

report_urls = [
    path(
        'visit-by-country',
        distribution_views.VisitByCountryDistributionSnapReportView.as_view(),
        name='visit-by-country-distribution-snap-report'
    ),
    path(
        'visit-by-city',
        distribution_views.VisitByCityDistributionSnapReportView.as_view(),
        name='visit-by-city-distribution-snap-report'
    ),
    path(
        'visit-by-channel',
        distribution_views.VisitByChannelDistributionSnapReportView.as_view(),
        name='visit-by-channel-distribution-snap-report'
    ),
    path(
        'sku-by-city',
        distribution_views.SKUByCityDistributionSnapReportView.as_view(),
        name='sku-by-city-distribution-snap-report'
    ),
    path(
        'sku-by-channel',
        distribution_views.SKUByChannelDistributionSnapReportView.as_view(),
        name='sku-by-channel-distribution-snap-report'
    )
]

urlpatterns = [
    path(
        'import',
        distribution_views.ImportDistributionSnapView.as_view(),
        name='import-distribution-snap'
    ),
    path(
        'export',
        distribution_views.ExportDistributionSnapView.as_view(),
        name='export-distribution-snap'
    ),
    path(
        'list',
        distribution_views.ListDistributionSnapView.as_view(),
        name='list-distribution-snap'
    ),
    path(
        '<str:distribution_snap_id>/update',
        distribution_views.UpdateDistributionSnapView.as_view(),
        name='update-distribution-snap'
    ),
    path(
        '<str:distribution_snap_id>/delete',
        distribution_views.DeleteDistributionSnapView.as_view(),
        name='delete-distribution-snap'
    ),
    path(
        'bulk-delete',
        distribution_views.BulkDeleteDistributionSnapView.as_view(),
        name='bulk-delete-distribution-snap'
    ),
    path(
        'report/',
        include(report_urls)
    )
]
