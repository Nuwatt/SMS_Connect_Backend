from django.urls import path, include

urlpatterns = [
    path(
        'sku/',
        include('apps.product.urls.sku_urls')
    ),
    path(
        'category/',
        include('apps.product.urls.category_urls')
    ),
    path(
        'product/',
        include('apps.product.urls.brand_urls')
    )
]
