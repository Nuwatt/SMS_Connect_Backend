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
    # path(
    #     'city-mode',
    #     new_price_monitor_views.CityModePriceMonitorSnapReportView.as_view(),
    #     name='city-mode-price-monitor-snap-report'
    # ),

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
    # path(
    #     'city-mode',
    #     new_price_monitor_views.CityModePriceMonitorSnapReportView.as_view(),
    #     name='city-mode-price-monitor-snap-report'
    # ),

    # channel
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
    # path(
    #     'city-mode',
    #     new_price_monitor_views.CityModePriceMonitorSnapReportView.as_view(),
    #     name='city-mode-price-monitor-snap-report'
    # ),
]
