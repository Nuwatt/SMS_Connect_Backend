from django.urls import path

from apps.snap.views import filters_views

urlpatterns = [
    path(
        'sku-list',
        filters_views.ListSKUFiltersView.as_view(),
        name='list-sku-filters'
    ),
    path(
        'brand-list',
        filters_views.ListBrandFiltersView.as_view(),
        name='list-brand-filters'
    ),
    path(
        'category-list',
        filters_views.ListCategoryFiltersView.as_view(),
        name='list-category-filters'
    ),
    path(
        'city-list',
        filters_views.ListCityFiltersView.as_view(),
        name='list-city-filters'
    ),
    path(
        'country-list',
        filters_views.ListCountryFiltersView.as_view(),
        name='list-country-filters'
    ),
    path(
        'channel-list',
        filters_views.ListChannelFiltersView.as_view(),
        name='list-channel-filters'
    )
]
