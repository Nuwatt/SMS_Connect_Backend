from apps.core import usecases
from apps.question.exceptions import QuestionTypeNotFound
from apps.question.models import QuestionType


class GetQuestionTypeUseCase(usecases.BaseUseCase):
    def __init__(self, question_type_id: str):
        self._question_type_id = question_type_id

    def execute(self):
        self._factory()
        return self._question_type

    def _factory(self):
        try:
            self._question_type = QuestionType.objects.get(pk=self._question_type_id)
        except QuestionType.DoesNotExist:
            raise QuestionTypeNotFound


class AddQuestionTypeUseCase(usecases.CreateUseCase):
    def _factory(self):
        QuestionType.objects.create(
            **self._data
        )


class ListQuestionTypeUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._question_types

    def _factory(self):
        self._question_types = QuestionType.objects.unarchived()

