from django.urls import path, include

from apps.snap.views import new_distribution_views, distribution_views

report_urls = [
    path(
        'city-report',
        new_distribution_views.DistributionSnapCityReportView.as_view(),
        name='distribution-snap-city-report'
    ),
    path(
        'country-report',
        new_distribution_views.DistributionSnapCountryReportView.as_view(),
        name='distribution-snap-country-report'
    ),
    path(
        'sku-report',
        new_distribution_views.DistributionSnapSKUReportView.as_view(),
        name='distribution-snap-sku-report'
    ),
    path(
        'brand-report',
        new_distribution_views.DistributionSnapBrandReportView.as_view(),
        name='distribution-snap-brand-report'
    ),
    path(
        'channel-report',
        new_distribution_views.DistributionSnapChannelReportView.as_view(),
        name='distribution-snap-channel-report'
    ),
    # path(
    #     'visit-by-city',
    #     distribution_views.VisitByCityDistributionSnapReportView.as_view(),
    #     name='visit-by-city-distribution-snap-report'
    # ),
    # path(
    #     'visit-by-channel',
    #     distribution_views.VisitByChannelDistributionSnapReportView.as_view(),
    #     name='visit-by-channel-distribution-snap-report'
    # ),
    # path(
    #     'sku-by-city',
    #     distribution_views.SKUByCityDistributionSnapReportView.as_view(),
    #     name='sku-by-city-distribution-snap-report'
    # ),
    path(
        'total-distribution',
        distribution_views.TotalDistributionSnapReportView.as_view(),
        name='total-distribution-snap-report'
    ),
    path(
        'shelf-share',
        distribution_views.ShelfShareDistributionSnapReportView.as_view(),
        name='shelf-share-distribution-snap-report'
    ),
    path(
        'number-of-outlet',
        distribution_views.NumberOfOutletDistributionSnapReportView.as_view(),
        name='number-of-outlet-distribution-snap-report'
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
