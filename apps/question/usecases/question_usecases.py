import csv
from io import StringIO

from django.core.exceptions import ValidationError as DjangoValidationError
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.product.models import Brand, SKU
from apps.question.exceptions import QuestionNotFound
from apps.question.models import Question, QuestionOption, QuestionType
from apps.questionnaire.models import Questionnaire
from apps.user.models import AgentUser


class GetQuestionUseCase(usecases.BaseUseCase):
    def __init__(self, question_id: str):
        self._question_id = question_id

    def execute(self):
        self._factory()
        return self._question

    def _factory(self):
        try:
            self._question = Question.objects.get(pk=self._question_id)
        except Question.DoesNotExist:
            raise QuestionNotFound


class AddQuestionUseCase(usecases.CreateUseCase):
    def __init__(self, serializer, questionnaire: Questionnaire):
        super().__init__(serializer)
        self._questionnaire = questionnaire

    def _factory(self):
        # 1. pop question options and question statement
        question_options_data = self._data.pop('question_options', None)

        # 2. create question
        question = Question(
            questionnaire=self._questionnaire,
            **self._data
        )
        try:
            question.full_clean()
            question.save()
        except DjangoValidationError as e:
            raise ValidationError(e.message_dict)

        # 3. create question options
        if question_options_data:
            question_options = []
            for data in question_options_data:
                question_options.append(
                    QuestionOption(
                        question=question,
                        option=data
                    )
                )
            QuestionOption.objects.bulk_create(question_options)


class ListQuestionUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._questions

    def _factory(self):
        self._questions = Question.objects.unarchived()


class ImportQuestionUseCase(usecases.ImportCSVUseCase):
    def __init__(self, serializer, questionnaire: Questionnaire):
        super().__init__(serializer)
        self._questionnaire = questionnaire

    valid_columns = ['Question Type', 'Question Text', 'Options', 'Brand', 'SKU']
    null_columns = ['Options']

    def _factory(self):
        # create question
        for item in self._item_list:
            # 1. get question_type
            try:
                question_type = QuestionType.objects.get(name=item.get('Question Type'))
            except QuestionType.DoesNotExist:
                raise ValidationError({
                    'non_field_errors': _('Invalid Question Type')
                })

            # # 2. brand
            # try:
            #     brand = Brand.objects.get(name=item.get('Brand'))
            # except Brand.DoesNotExist:
            #     raise ValidationError({
            #         'non_field_errors': _('Invalid Brand')
            #     })

            # 3. brand
            try:
                sku = SKU.objects.get(name=item.get('SKU'))
            except SKU.DoesNotExist:
                raise ValidationError({
                    'non_field_errors': _('Invalid SKU')
                })

            # 4. options
            options = item.get('Options').split(',')

            # 6. update or create question
            question, created = Question.objects.update_or_create(
                questionnaire=self._questionnaire,
                statement=item.get('Question Text'),
                defaults={
                    # 'brand': brand,
                    'sku': sku,
                    'question_type': question_type
                }
            )

            if question.question_type.has_options:
                if not options[0]:
                    raise ValidationError({
                        'non_field_errors': _('Options required for this question type')
                    })
                for option in options:
                    question_option, created = QuestionOption.objects.get_or_create(
                        question=question,
                        option=option
                    )


class ExportQuestionUseCase(usecases.BaseUseCase):
    columns = ['Question Type', 'Question Text', 'Options', 'Brand', 'SKU']

    def __init__(self, questionnaire: Questionnaire):
        self._questionnaire = questionnaire

    def execute(self):
        return self._factory()

    def _factory(self):
        response = HttpResponse(content_type='text/csv')
        filename = '{}.csv'.format(self._questionnaire.id)
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

        # 1. write headers
        writer = csv.writer(response)
        writer.writerow(self.columns)

        # 2. write questions
        questions = self._questionnaire.question_set.unarchived()
        for question in questions:
            options = question.questionoption_set.unarchived().values_list('option', flat=True)
            writer.writerow([
                question.question_type,
                question.statement,
                ','.join(options),
                question.sku.brand,
                question.sku
            ])
        return response


class ListQuestionForAgentUseCase(usecases.BaseUseCase):
    def __init__(self, agent_user: AgentUser, questionnaire: Questionnaire):
        self._agent_user = agent_user
        self._questionnaire = questionnaire

    def execute(self):
        self.is_valid()
        self._factory()
        return self._questions

    def _factory(self):
        self._questions = self._questionnaire.question_set.unarchived().select_related(
            'question_type'
        )

    def is_valid(self):
        # 1. check if agent has access to questionnaire
        if not self._questionnaire.has_access_for_agent(agent=self._agent_user):
            raise ValidationError({
                'non_field_errors': _('Questionnaire is not assigned to agent.')
            })
