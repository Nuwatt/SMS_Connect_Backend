from django.urls import path

from apps.market.views import store_views

urlpatterns = [
    path(
        'add',
        store_views.AddStoreView.as_view(),
        name='add-store'

    ),
    path(
        'agent-user/add',
        store_views.AddStoreView.as_view(),
        name='add-store'

    ),
    path(
        'list',
        store_views.ListStoreView.as_view(),
        name='list-store'

    ),
    path(
        '<str:store_id>/update',
        store_views.UpdateStoreView.as_view(),
        name='update-store'

    ),
    path(
        '<str:store_id>/delete',
        store_views.DeleteStoreView.as_view(),
        name='delete-store'

    )
]
