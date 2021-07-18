from django.db.models import Count, F, Q, Avg
from sql_util.aggregates import SubqueryCount

from apps.core import usecases
from apps.response.models import Response, OptionAnswer, ChoiceAnswer, NumericAnswer


class YesNoQuestionReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Consumer Question',
            answer__response__is_completed=True,
            answer__question__question_type__name='Yes or No',
            is_archived=False
        ).annotate(
            question=F('answer__question'),
        ).values(
            'question'
        ).annotate(
            total_answer=Count('choice'),
            yes=Count(
                'choice',
                filter=Q(choice__choice='Yes')
            ) / F('total_answer') * 100,
            no=Count(
                'choice',
                filter=Q(choice__choice='No')
            ) / F('total_answer') * 100,
            question_statement=F('answer__question__statement')
        ).values(
            'yes',
            'no',
            'question_statement'
        )


class RatingOneToThreeReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Consumer Question',
            answer__response__is_completed=True,
            answer__question__question_type__name='Rating 1 to 3',
            is_archived=False
        ).annotate(
            question=F('answer__question'),
        ).values(
            'question'
        ).annotate(
            total_answer=Count('choice'),
            rating_one=Count(
                'choice',
                filter=Q(
                    choice__choice='1',
                    choice__question_type__name='Rating 1 to 3'
                )
            ) / F('total_answer') * 100,
            rating_two=Count(
                'choice',
                filter=Q(
                    choice__choice='2',
                    choice__question_type__name='Rating 1 to 3'
                )
            ) / F('total_answer') * 100,
            rating_three=Count(
                'choice',
                filter=Q(
                    choice__choice='3',
                    choice__question_type__name='Rating 1 to 3'
                )
            ) / F('total_answer') * 100,
            question_statement=F('answer__question__statement'),
        ).values(
            'rating_one',
            'rating_two',
            'rating_three',
            'question_statement',
        )


class RatingOneToFiveReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Consumer Question',
            answer__response__is_completed=True,
            answer__question__question_type__name='Rating 1 to 5',
            is_archived=False
        ).annotate(
            question=F('answer__question'),
        ).values(
            'question'
        ).annotate(
            total_answer=Count('choice'),
            rating_one=Count(
                'choice',
                filter=Q(
                    choice__choice='1',
                    choice__question_type__name='Rating 1 to 5'
                )
            ) / F('total_answer') * 100,
            rating_two=Count(
                'choice',
                filter=Q(
                    choice__choice='2',
                    choice__question_type__name='Rating 1 to 5'
                )
            ) / F('total_answer') * 100,
            rating_three=Count(
                'choice',
                filter=Q(
                    choice__choice='3',
                    choice__question_type__name='Rating 1 to 5'
                )
            ) / F('total_answer') * 100,
            rating_four=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    choice__choice='4',
                    choice__question_type__name='Rating 1 to 5'
                )
            ) / F('total_answer') * 100,
            rating_five=Count(
                'answer__choiceanswer__choice',
                filter=Q(
                    choice__choice='5',
                    choice__question_type__name='Rating 1 to 5'
                )
            ) / F('total_answer') * 100,
            question_statement=F('answer__question__statement'),
        ).values(
            'rating_one',
            'rating_two',
            'rating_three',
            'rating_four',
            'rating_five',
            'question_statement'
        )


class RatingOneToTenReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Consumer Question',
            answer__response__is_completed=True,
            answer__question__question_type__name='Rating 1 to 10',
            is_archived=False
        ).annotate(
            question=F('answer__question'),
        ).values(
            'question'
        ).annotate(
            total_answer=Count('choice'),
            rating_one=Count(
                'choice',
                filter=Q(
                    choice__choice='1',
                    choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_two=Count(
                'choice',
                filter=Q(
                    choice__choice='2',
                    choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_three=Count(
                'choice',
                filter=Q(
                    choice__choice='3',
                    choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_four=Count(
                'choice',
                filter=Q(
                    choice__choice='4',
                    choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_five=Count(
                'choice',
                filter=Q(
                    choice__choice='5',
                    choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_six=Count(
                'choice',
                filter=Q(
                    choice__choice='6',
                    choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_seven=Count(
                'choice',
                filter=Q(
                    choice__choice='7',
                    choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_eight=Count(
                'choice',
                filter=Q(
                    choice__choice='8',
                    choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_nine=Count(
                'choice',
                filter=Q(
                    choice__choice='9',
                    choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            rating_ten=Count(
                'choice',
                filter=Q(
                    choice__choice='10',
                    choice__question_type__name='Rating 1 to 10'
                )
            ) / F('total_answer') * 100,
            question_statement=F('answer__question__statement'),
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
        )


class NumericQuestionReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = NumericAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Consumer Question',
            answer__question__question_type__name='Numeric',
            answer__question__is_completed=True
        ).annotate(
            question=F('answer__question'),
        ).values(
            'question'
        ).annotate(
            value=Avg('numeric'),
            question_statement=F('answer__question__statement'),
        ).values(
            'value',
            'question_statement',
        )


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
