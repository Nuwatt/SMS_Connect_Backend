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
    # total sku per city
    path(
        'sku-per-city',
        distribution_check_views.SKUPerCityReportView.as_view(),
        name='sku-per-city-report'
    ),
    # total sku per country
    path(
        'sku-per-country',
        distribution_check_views.SKUPerCountryReportView.as_view(),
        name='sku-per-country-report'
    ),
    # total sku per channel
    path(
        'sku-per-channel',
        distribution_check_views.SKUPerChannelReportView.as_view(),
        name='sku-per-channel-report'
    ),
    # total brand per city
    path(
        'brand-per-city',
        distribution_check_views.BrandPerCityReportView.as_view(),
        name='sku-per-channel-report'
    ),
    # total sku per country
    path(
        'brand-per-country',
        distribution_check_views.BrandPerCountryReportView.as_view(),
        name='brand-per-country-report'
    ),
    # total sku per channel
    path(
        'brand-per-channel',
        distribution_check_views.BrandPerChannelReportView.as_view(),
        name='brand-per-channel-report'
    ),
    # avg per sku
    path(
        'avg-per-sku',
        distribution_check_views.AvgPerSKUReportView.as_view(),
        name='avg-per-sku-report'
    ),
    # avg per brand
    path(
        'avg-per-brand',
        distribution_check_views.AvgPerBrandReportView.as_view(),
        name='avg-per-brand-report'
    ),
    # avg per channel
    path(
        'avg-per-channel',
        distribution_check_views.AvgPerChannelReportView.as_view(),
        name='avg-per-channel-report'
    ),
]
