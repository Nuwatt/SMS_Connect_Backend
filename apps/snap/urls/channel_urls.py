from django.urls import path

from apps.snap.views import channel_views

urlpatterns = [
    path(
        'add',
        channel_views.AddSnapChannelView.as_view(),
        name='add-snap-channel'
    ),
    path(
        'list',
        channel_views.ListSnapChannelView.as_view(),
        name='list-snap-channel'
    ),
    path(
        '<str:snap_channel_id>/update',
        channel_views.UpdateSnapChannelView.as_view(),
        name='update-snap-channel'
    ),
    path(
        '<str:snap_channel_id>/delete',
        channel_views.DeleteSnapChannelView.as_view(),
        name='delete-snap-channel'
    )
]
