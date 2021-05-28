from django.db import models
from django.db.models import Count, Case, When

from apps.core import usecases
from apps.localize.models import City, Country
from apps.product.models import SKU
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


class SKUReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        price_monitor = QuestionnaireType.objects.get(name__iexact='price monitor')

        self._results = NumericAnswer.objects.filter(
            answer__question__questionnaire__questionnaire_type=price_monitor
        )


class SKUMonthReportUseCase(SKUReportUseCase):
    pass


class SKUCountryReportUseCase(SKUReportUseCase):
    pass


class AnswerPerCountryReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Country.objects.annotate(
            value=Count('retailer__response')
        ).values('name', 'value')


class AnswerPerCityReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = City.objects.annotate(
            value=Count('retailer__response')
        ).values('name', 'value')


class AnswerPerSKUReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.annotate(
            value=Count('question__answer__response')
        ).values('name', 'value')
