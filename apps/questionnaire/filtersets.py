from django_filters import rest_framework as filters

from apps.questionnaire.models import Questionnaire


class QuestionnaireFilter(filters.FilterSet):
    class Meta:
        model = Questionnaire
        fields = [
            'questionnaire_type',
            'city',
            'category',
        ]


class AvailableQuestionnaireForAgentFilter(filters.FilterSet):
    class Meta:
        model = Questionnaire
        fields = [
            'questionnaire_type',
        ]
