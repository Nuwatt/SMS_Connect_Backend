from django_filters import rest_framework as filters

from apps.question.models import Question
from apps.questionnaire.models import Questionnaire


class QuestionFilter(filters.FilterSet):
    class Meta:
        model = Question
        fields = [
            'questionnaire',
        ]
