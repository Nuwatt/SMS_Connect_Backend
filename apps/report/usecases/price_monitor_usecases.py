from django.db.models import Count

from apps.core import usecases
from apps.questionnaire.models import QuestionnaireType
from apps.response.models import NumericAnswer


class SKUMinMaxReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        price_monitor = QuestionnaireType.objects.get(name__iexact='price monitor')

        self._results = NumericAnswer.objects.filter(
            answer__question__questionnaire__questionnaire_type=price_monitor
        ).annotate(
            frequency=Count('numeric')
        )
