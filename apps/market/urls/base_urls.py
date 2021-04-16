from django.urls import path, include

urlpatterns = [
    path(
        'store/',
        include('apps.market.urls.store_urls')
    ),
    path(
        'retailer/',
        include('apps.market.urls.retailer_urls')
    ),
]
