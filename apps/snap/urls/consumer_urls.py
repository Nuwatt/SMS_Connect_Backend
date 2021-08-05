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
#     path(
#         'month-max',
#         price_monitor_views.MonthMaxPriceMonitorSnapReportView.as_view(),
#         name='month-max-price-monitor-snap-report'
#     ),
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
        consumer_views.ImportConsumerSnapView.as_view(),
        name='import-consumer-snap'
    ),
    path(
        'list',
        consumer_views.ListConsumerSnapView.as_view(),
        name='list-consumer-snap'
    ),
    path(
        '<str:price_monitor_snap_id>/update',
        consumer_views.UpdateConsumerSnapView.as_view(),
        name='update-consumer-snap'
    ),
    path(
        '<str:price_monitor_snap_id>/delete',
        consumer_views.DeleteConsumerSnapView.as_view(),
        name='delete-consumer-snap'
    ),
    path(
        'report/',
        include(report_urls)
    )
]
