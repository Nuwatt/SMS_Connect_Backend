from django.urls import path

from apps.terms_and_conditions import views

urlpatterns = [
    path(
        'add',
        views.AddTermsAndConditionsView.as_view(),
        name='add-terms-and-conditions'

    ),
    path(
        'detail',
        views.TermsAndConditionsDetailView.as_view(),
        name='terms-and-conditions-detail'

    ),
    path(
        'update',
        views.UpdateTermsAndConditionsView.as_view(),
        name='update-terms-and-conditions'

    ),
    path(
        'delete',
        views.DeleteTermsAndConditionsView.as_view(),
        name='delete-terms-and-conditions'

    )
]
