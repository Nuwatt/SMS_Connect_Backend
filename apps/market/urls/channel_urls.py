from django.urls import path

from apps.market.views import channel_views

urlpatterns = [
    path(
        'add',
        channel_views.AddChannelView.as_view(),
        name='add-channel'

    ),
    path(
        'list',
        channel_views.ListChannelView.as_view(),
        name='list-channel'

    ),
    path(
        '<str:channel_id>/update',
        channel_views.UpdateChannelView.as_view(),
        name='update-channel'

    ),
    path(
        '<str:channel_id>/delete',
        channel_views.DeleteChannelView.as_view(),
        name='delete-channel'

    )
]
