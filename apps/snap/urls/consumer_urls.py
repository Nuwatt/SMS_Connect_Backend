from django.urls import path, include

from apps.snap.views import consumer_views

report_urls = [
    path(
        'yes-no-question',
        consumer_views.YesNoQuestionSnapConsumerReportView.as_view(),
        name='Yes-no-question-consumer-snap-report'
    ),
    path(
        'rating-one-to-three',
        consumer_views.RatingOneToThreeSnapConsumerReportView.as_view(),
        name='rating-one-to-three-consumer-snap-report'
    ),
    path(
        'rating-one-to-five',
        consumer_views.RatingOneToFiveSnapConsumerReportView.as_view(),
        name='rating-one-to-five-consumer-snap-report'
    ),
    path(
        'rating-one-to-ten',
        consumer_views.RatingOneToTenSnapConsumerReportView.as_view(),
        name='rating-one-to-ten-consumer-snap-report'
    ),
    path(
        'numeric-average',
        consumer_views.NumericAverageSnapConsumerReportView.as_view(),
        name='numeric-average-consumer-snap-report'
    ),
]

urlpatterns = [
    path(
        'import',
        consumer_views.ImportSnapConsumerView.as_view(),
        name='import-consumer-snap'
    ),
    path(
        'export',
        consumer_views.ExportSnapConsumerView.as_view(),
        name='export-consumer-snap'
    ),
    path(
        'list',
        consumer_views.ListSnapConsumerView.as_view(),
        name='list-consumer-snap'
    ),
    path(
        '<str:consumer_snap_id>/update',
        consumer_views.UpdateSnapConsumerView.as_view(),
        name='update-consumer-snap'
    ),
    path(
        '<str:consumer_snap_id>/delete',
        consumer_views.DeleteSnapConsumerView.as_view(),
        name='delete-consumer-snap'
    ),
    path(
        'bulk-delete',
        consumer_views.BulkDeleteOutOfStockSnapView.as_view(),
        name='bulk-delete-consumer-snap'
    ),
    path(
        'report/',
        include(report_urls)
    )
]
