from django.urls import path

from apps.report.views import consumer_questionnaire_views

urlpatterns = [
    # yes-no-question
    path(
        'yes-no-question',
        consumer_questionnaire_views.YesNoQuestionReportView.as_view(),
        name='yes-no-question'
    ),
    # rating-1-to-3
    path(
        'rating-one-to-three',
        consumer_questionnaire_views.RatingOneToThreeReportView.as_view(),
        name='rating-one-to-three'
    ),
    # rating-1-to-5
    path(
        'rating-one-to-five',
        consumer_questionnaire_views.RatingOneToFiveReportView.as_view(),
        name='rating-one-to-five'
    ),
    # rating-1-to-5
    path(
        'rating-one-to-ten',
        consumer_questionnaire_views.RatingOneToTenReportView.as_view(),
        name='rating-one-to-ten'
    ),
    # numeric
    path(
        'numeric-question',
        consumer_questionnaire_views.NumericQuestionReportView.as_view(),
        name='numeric-question'
    ),
]
