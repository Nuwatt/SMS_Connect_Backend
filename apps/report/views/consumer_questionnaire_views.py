from apps.report.filtersets.base_filtersets import SKUResponseFilter, ResponseFilter
from apps.report.serializers import consumer_questionnaire_serializers
from apps.report.usecases import consumer_questionnaire_usecases

from apps.report.views.base_views import BaseReportView


class YesNoQuestionReportView(BaseReportView):
    """
    Use this end-point to list report of total yes no question for consumer questionnaire
    """
    serializer_class = consumer_questionnaire_serializers.YesNoQuestionReportSerializer
    filterset_class = SKUResponseFilter

    def get_queryset(self):
        return consumer_questionnaire_usecases.YesNoQuestionReportUseCase().execute()


class RatingOneToThreeReportView(BaseReportView):
    """
    Use this end-point to list report of total rating 1 to 3 question for consumer questionnaire
    """
    serializer_class = consumer_questionnaire_serializers.RatingOneToThreeReportSerializer
    filterset_class = SKUResponseFilter

    def get_queryset(self):
        return consumer_questionnaire_usecases.RatingOneToThreeReportUseCase().execute()


class RatingOneToFiveReportView(BaseReportView):
    """
    Use this end-point to list report of total rating 1 to 5 question for consumer questionnaire
    """
    serializer_class = consumer_questionnaire_serializers.RatingOneToFiveReportSerializer
    filterset_class = SKUResponseFilter

    def get_queryset(self):
        return consumer_questionnaire_usecases.RatingOneToFiveReportUseCase().execute()


class RatingOneToTenReportView(BaseReportView):
    """
    Use this end-point to list report of total rating 1 to 10 question for consumer questionnaire
    """
    serializer_class = consumer_questionnaire_serializers.RatingOneToTenReportSerializer
    filterset_class = SKUResponseFilter

    def get_queryset(self):
        return consumer_questionnaire_usecases.RatingOneToTenReportUseCase().execute()


class NumericQuestionReportView(BaseReportView):
    """
    Use this end-point to list report of average numeric answer for consumer questionnaire
    """
    serializer_class = consumer_questionnaire_serializers.NumericQuestionReportSerializer
    filterset_class = SKUResponseFilter

    def get_queryset(self):
        return consumer_questionnaire_usecases.NumericQuestionReportUseCase().execute()


class OptionsQuestionReportView(BaseReportView):
    """
    Use this end-point to list report of  options answer for consumer questionnaire
    """
    serializer_class = consumer_questionnaire_serializers.OptionsQuestionReportSerializer
    filterset_class = SKUResponseFilter

    def get_queryset(self):
        return consumer_questionnaire_usecases.OptionsQuestionReportUseCase().execute()
