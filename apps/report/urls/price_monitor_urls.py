from django.urls import path, include

from apps.report.views import price_monitor_views

urlpatterns = [
    path(
        'min-max',
        price_monitor_views.SKUMinMaxReportView.as_view(),
        name='sku-min-max-report'
    ),
    # sku vs month
    path(
        'month-max',
        price_monitor_views.SKUMonthMaxReportView.as_view(),
        name='sku-month-max-report'
    ),
    path(
        'month-min',
        price_monitor_views.SKUMonthMinReportView.as_view(),
        name='sku-month-min-report'
    ),
    path(
        'month-mean',
        price_monitor_views.SKUMonthMeanReportView.as_view(),
        name='sku-month-mean-report'
    ),
    path(
        'month-mode',
        price_monitor_views.SKUMonthModeReportView.as_view(),
        name='sku-month-mode-report'
    ),
    # sku vs country
    path(
        'country-max',
        price_monitor_views.SKUCountryMaxReportView.as_view(),
        name='sku-country-max-report'
    ),
    path(
        'country-min',
        price_monitor_views.SKUCountryMinReportView.as_view(),
        name='sku-country-min-report'
    ),
    path(
        'country-mean',
        price_monitor_views.SKUCountryMeanReportView.as_view(),
        name='sku-country-mean-report'
    ),
    path(
        'country-mode',
        price_monitor_views.SKUCountryModeReportView.as_view(),
        name='sku-country-mode-report'
    ),
    # answer per country
    path(
        'answer-per-country',
        price_monitor_views.AnswerPerCountryReportView.as_view(),
        name='answer-per-country-report'
    ),
    # answer per city
    path(
        'answer-per-city',
        price_monitor_views.AnswerPerCityReportView.as_view(),
        name='answer-per-city-report'
    ),
    # answer per sku
    path(
        'answer-per-sku',
        price_monitor_views.AnswerPerSKUReportView.as_view(),
        name='answer-per-sku-report'
    ),
    # brand min-max
    path(
        'brand-min-max',
        price_monitor_views.BrandMinMaxReportView.as_view(),
        name='brand-min-max-report'
    ),

]
