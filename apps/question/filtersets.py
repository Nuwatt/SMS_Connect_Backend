from django_filters import rest_framework as filters

from apps.question.models import Question
from apps.questionnaire.usecases.questionnaire_usecases import GetQuestionnaireUseCase


class QuestionFilter(filters.FilterSet):
    class Meta:
        model = Question
        fields = [
            'questionnaire',
        ]


class QuestionTypeFilter(filters.FilterSet):
    questionnaire = filters.CharFilter(
        method='questionnaire_filter',
        label='questionnaire'
    )

    def questionnaire_filter(self, queryset, name, value):
        questionnaire_type = GetQuestionnaireUseCase(
            questionnaire_id=value
        ).execute().questionnaire_type
        if questionnaire_type.name == 'Price Monitor':
            return queryset.filter(
                name__icontains='numeric'
            )
        elif questionnaire_type.name == 'Out Of Stock':
            return queryset.filter(
                name__icontains='oos question'
            )
        return queryset
