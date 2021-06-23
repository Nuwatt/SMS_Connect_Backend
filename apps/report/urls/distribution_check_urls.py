from django.urls import path

from apps.report.views import distribution_check_views

urlpatterns = [
    # visit per country
    path(
        'visit-per-country',
        distribution_check_views.VisitPerCountryReportView.as_view(),
        name='visit-per-country-report'
    ),
    # visit per city
    path(
        'visit-per-city',
        distribution_check_views.VisitPerCityReportView.as_view(),
        name='visit-per-city-report'
    ),
    # visit per city
    path(
        'visit-per-channel',
        distribution_check_views.VisitPerChannelReportView.as_view(),
        name='visit-per-channel-report'
    ),
    # # total sku per city
    # path(
    #     'sku-per-city',
    #     distribution_check_views.SKUPerCityReportView.as_view(),
    #     name='sku-per-city-report'
    # ),
]
