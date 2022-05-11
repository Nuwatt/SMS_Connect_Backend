from django.urls import path

from apps.snap.views import new_price_monitor_views

urlpatterns = [
    # city
    path(
        'city-max',
        new_price_monitor_views.CityMaxPriceMonitorSnapReportView.as_view(),
        name='city-max-price-monitor-snap-report'
    ),
    path(
        'city-min',
        new_price_monitor_views.CityMinPriceMonitorSnapReportView.as_view(),
        name='city-min-price-monitor-snap-report'
    ),
    path(
        'city-mean',
        new_price_monitor_views.CityMeanPriceMonitorSnapReportView.as_view(),
        name='city-mean-price-monitor-snap-report'
    ),
    path(
        'city-mode',
        new_price_monitor_views.CityModePriceMonitorSnapReportView.as_view(),
        name='city-mode-price-monitor-snap-report'
    ),

    # channel
    path(
        'channel-max',
        new_price_monitor_views.ChannelMaxPriceMonitorSnapReportView.as_view(),
        name='channel-max-price-monitor-snap-report'
    ),
    path(
        'channel-min',
        new_price_monitor_views.ChannelMinPriceMonitorSnapReportView.as_view(),
        name='channel-min-price-monitor-snap-report'
    ),
    path(
        'channel-mean',
        new_price_monitor_views.ChannelMeanPriceMonitorSnapReportView.as_view(),
        name='channel-mean-price-monitor-snap-report'
    ),
    path(
        'channel-mode',
        new_price_monitor_views.ChannelModePriceMonitorSnapReportView.as_view(),
        name='channel-mode-price-monitor-snap-report'
    ),

    # brand
    path(
        'brand-max',
        new_price_monitor_views.BrandMaxPriceMonitorSnapReportView.as_view(),
        name='brand-max-price-monitor-snap-report'
    ),
    path(
        'brand-min',
        new_price_monitor_views.BrandMinPriceMonitorSnapReportView.as_view(),
        name='brand-min-price-monitor-snap-report'
    ),
    path(
        'brand-mean',
        new_price_monitor_views.BrandMeanPriceMonitorSnapReportView.as_view(),
        name='brand-mean-price-monitor-snap-report'
    ),
    path(
        'brand-mode',
        new_price_monitor_views.BrandModePriceMonitorSnapReportView.as_view(),
        name='brand-mode-price-monitor-snap-report'
    ),

    # channel city
    path(
        'channel-city-max',
        new_price_monitor_views.ChannelCityMaxPriceMonitorSnapReportView.as_view(),
        name='channel-city-max-price-monitor-snap-report'
    ),
    path(
        'channel-city-min',
        new_price_monitor_views.ChannelCityMinPriceMonitorSnapReportView.as_view(),
        name='channel-city-min-price-monitor-snap-report'
    ),
    path(
        'channel-city-mean',
        new_price_monitor_views.ChannelCityMeanPriceMonitorSnapReportView.as_view(),
        name='channel-city-mean-price-monitor-snap-report'
    ),
    path(
        'channel-city-mode',
        new_price_monitor_views.ChannelCityModePriceMonitorSnapReportView.as_view(),
        name='channel-city-mode-price-monitor-snap-report'
    ),
]
