from django.urls import path, include

from apps.snap.views import consumer_views

report_urls = [
    path(
        'yes-no-question',
        consumer_views.YesNoQuestionConsumerSnapReportView.as_view(),
        name='Yes-no-question-consumer-snap-report'
    ),
    path(
        'rating-one-to-three',
        consumer_views.RatingOneToThreeConsumerSnapReportView.as_view(),
        name='rating-one-to-three-consumer-snap-report'
    ),
    path(
        'rating-one-to-five',
        consumer_views.RatingOneToFiveConsumerSnapReportView.as_view(),
        name='rating-one-to-five-consumer-snap-report'
    ),
    path(
        'rating-one-to-ten',
        consumer_views.RatingOneToTenConsumerSnapReportView.as_view(),
        name='rating-one-to-ten-consumer-snap-report'
    ),
    path(
        'numeric-average',
        consumer_views.NumericAverageConsumerSnapReportView.as_view(),
        name='numeric-average-consumer-snap-report'
    ),
]

urlpatterns = [
    path(
        'import',
        consumer_views.ImportConsumerSnapView.as_view(),
        name='import-consumer-snap'
    ),
    path(
        'list',
        consumer_views.ListConsumerSnapView.as_view(),
        name='list-consumer-snap'
    ),
    path(
        '<str:consumer_snap_id>/update',
        consumer_views.UpdateConsumerSnapView.as_view(),
        name='update-consumer-snap'
    ),
    path(
        '<str:consumer_snap_id>/delete',
        consumer_views.DeleteConsumerSnapView.as_view(),
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
