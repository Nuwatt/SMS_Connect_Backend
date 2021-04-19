from apps.core import usecases
from apps.question.exceptions import QuestionNotFound
from apps.question.models import Question, QuestionStatement, QuestionOption


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
    def _factory(self):
        # 1. pop question options and question statement
        question_options_data = self._data.pop('question_options')
        question_statement_data = self._data.pop('question_statement')

        # 2. create question statement
        question_statement = QuestionStatement.objects.create(
            statement=question_statement_data
        )

        # 2. create question
        question = Question.objects.create(
            question_statement=question_statement,
            **self._data
        )

        # 3. create question options
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

