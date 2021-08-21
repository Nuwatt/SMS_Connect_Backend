from django.urls import path

from apps.snap.views import store_views

urlpatterns = [
    path(
        'add',
        store_views.AddSnapStoreView.as_view(),
        name='add-snap-store'

    ),
    path(
        'list',
        store_views.ListSnapStoreView.as_view(),
        name='list-snap-store'
    ),
    path(
        'basic-list',
        store_views.BasicListSnapStoreView.as_view(),
        name='basic-list-snap-store'
    ),
    path(
        '<str:store_id>/update',
        store_views.UpdateSnapStoreView.as_view(),
        name='update-snap-store'

    ),
    path(
        '<str:store_id>/delete',
        store_views.DeleteSnapStoreView.as_view(),
        name='delete-snap-store'

    )
]
