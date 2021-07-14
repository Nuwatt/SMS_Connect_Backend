from django.db.models import Count, F, Q, Avg
from sql_util.aggregates import SubqueryCount

from apps.core import usecases
from apps.response.models import Response, OptionAnswer


class YesNoQuestionReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Consumer Question',
            answer__question__question_type__name='Yes or No',
            is_completed=True
        ).annotate(
            question=F('answer__question'),
        ).values(
            'question'
        ).annotate(
            total_answer=Count('answer'),
            yes=Count(
                'answer__choiceanswer__choice',
                filter=Q(answer__choiceanswer__choice__choice='Yes')
            ) / F('total_answer') * 100,
            no=Count(
                'answer__choiceanswer__choice',
                filter=Q(answer__choiceanswer__choice__choice='No')
            ) / F('total_answer') * 100,
            brand=F('answer__question__sku__brand'),
            question_statement=F('answer__question__statement'),
            sku=F('answer__question__sku'),
        ).values(
            'yes',
            'no',
            'question_statement',
            'sku',
            'brand',
        ).unarchived()


class RatingOneToThreeReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Consumer Question',
            answer__question__question_type__name='Rating 1 to 3',
            is_completed=True
        ).annotate(
            question=F('answer__question'),
        ).values(
            'question'
        ).annotate(
            total_answer=Count('answer'),
            rating_one=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='1',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 3'
                )
            ) / F('total_answer') * 100,
            rating_two=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='2',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 3'
                )
            ) / F('total_answer') * 100,
            rating_three=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='3',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 3'
                )
            ) / F('total_answer') * 100,
            brand=F('answer__question__sku__brand'),
            question_statement=F('answer__question__statement'),
            sku=F('answer__question__sku'),
        ).values(
            'rating_one',
            'rating_two',
            'rating_three',
            'question_statement',
            'sku',
            'brand',
        ).unarchived()


class RatingOneToFiveReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Consumer Question',
            answer__question__question_type__name='Rating 1 to 5',
            is_completed=True
        ).annotate(
            question=F('answer__question'),
        ).values(
            'question'
        ).annotate(
            total_answer=Count('answer'),
            rating_one=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='1',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 5'
                )
            ) / F('total_answer') * 100,
            rating_two=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='2',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 5'
                )
            ) / F('total_answer') * 100,
            rating_three=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='3',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 5'
                )
            ) / F('total_answer') * 100,
            rating_four=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='4',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 5'
                )
            ) / F('total_answer') * 100,
            rating_five=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='5',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 5'
                )
            ) / F('total_answer') * 100,
            brand=F('answer__question__sku__brand'),
            question_statement=F('answer__question__statement'),
            sku=F('answer__question__sku'),
        ).values(
            'rating_one',
            'rating_two',
            'rating_three',
            'rating_four',
            'rating_five',
            'question_statement',
            'sku',
            'brand',
        ).unarchived()


class RatingOneToTenReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Consumer Question',
            answer__question__question_type__name='Rating 1 to 10',
            is_completed=True
        ).annotate(
            question=F('answer__question'),
        ).values(
            'question'
        ).annotate(
            total_answer=Count('answer'),
            rating_one=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='1',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_two=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='2',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_three=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='3',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_four=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='4',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_five=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='5',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_six=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='6',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_seven=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='7',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_eight=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='8',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_nine=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='9',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_ten=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    answer__choiceanswer__choice__choice='10',
                    answer__choiceanswer__choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            brand=F('answer__question__sku__brand'),
            question_statement=F('answer__question__statement'),
            sku=F('answer__question__sku'),
        ).values(
            'rating_one',
            'rating_two',
            'rating_three',
            'rating_four',
            'rating_five',
            'rating_six',
            'rating_seven',
            'rating_eight',
            'rating_nine',
            'rating_ten',
            'question_statement',
            'sku',
            'brand',
        ).unarchived()


class NumericQuestionReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Consumer Question',
            answer__question__question_type__name='Numeric',
            is_completed=True
        ).annotate(
            question=F('answer__question'),
        ).values(
            'question'
        ).annotate(
            value=Avg('answer__numericanswer__numeric'),
            brand=F('answer__question__sku__brand'),
            question_statement=F('answer__question__statement'),
            sku=F('answer__question__sku'),
        ).values(
            'value',
            'question_statement',
            'sku',
            'brand',
        ).unarchived()


class OptionsQuestionReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = OptionAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Consumer Question',
            answer__question__question_type__has_options=True,
            answer__response__is_completed=True,
            is_archived=False
        ).values(
            'answer__question',
        ).distinct().annotate(
            total_count=SubqueryCount('answer__question__questionoption'),
            value=Count('option') / F('total_count') * 100,
            question=F('answer__question'),
            option_text=F('option__option'),
            question_statement=F('answer__question__statement'),
        ).values(
            'question_statement',
            'question',
            'option_text',
            'value',
        )
