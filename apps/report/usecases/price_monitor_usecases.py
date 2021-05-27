from django.db.models import Max, Min, Avg, Count

from apps.core import usecases
from apps.product.models import SKU
from apps.questionnaire.models import QuestionnaireType
from apps.response.models import NumericAnswer


class SKUMinMaxReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        price_monitor = QuestionnaireType.objects.get(name__iexact='price monitor')
        # a = NumericAnswer.objects.filter(
        #         answer__question__questionnaire__questionnaire_type=price_monitor
        #     ).annotate(
        #         frequency=Count('numeric')
        #     ).order_by(
        #         '-frequency'
        #     ).values('numeric')
        #
        # answer_report = a.aggregate(
        #     max=Max('numeric'),
        #     min=Min('numeric'),
        #     mean=Avg('numeric'),
        # )
        self._results = []
        skus = SKU.objects.prefetch_related(
            'question_set__questionnaire__questionnaire_type',
            'question_set__answer_set'
        ).unarchived().iterator()
        for sku in skus:
            answer = NumericAnswer.objects.filter(
                answer__question__sku=sku,
                answer__question__questionnaire__questionnaire_type=price_monitor
            ).annotate(
                frequency=Count('numeric')
            ).order_by(
                '-frequency'
            ).values('numeric')

            answer_report = answer.aggregate(
                max=Max('numeric'),
                min=Min('numeric'),
                mean=Avg('numeric'),
            )

            self._results.append({
                'sku': sku,
                'max': answer_report.get('max'),
                'min': answer_report.get('min'),
                'mode': answer[0].get('numeric') if answer else None,
                'mean': answer_report.get('mean'),
            })
