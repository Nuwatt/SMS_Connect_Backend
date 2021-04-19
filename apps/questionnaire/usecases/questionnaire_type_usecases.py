from apps.core import usecases
from apps.questionnaire.exceptions import QuestionnaireTypeNotFound
from apps.questionnaire.models import QuestionnaireType


class GetQuestionnaireTypeUseCase(usecases.BaseUseCase):
    def __init__(self, questionnaire_type_id: str):
        self._questionnaire_type_id = questionnaire_type_id

    def execute(self):
        self._factory()
        return self._questionnaire_type

    def _factory(self):
        try:
            self._questionnaire_type = QuestionnaireType.objects.get(pk=self._questionnaire_type_id)
        except QuestionnaireType.DoesNotExist:
            raise QuestionnaireTypeNotFound


class AddQuestionnaireTypeUseCase(usecases.CreateUseCase):
    def _factory(self):
        QuestionnaireType.objects.create(**self._data)


class UpdateQuestionnaireTypeUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, questionnaire_type: QuestionnaireType):
        super().__init__(serializer, questionnaire_type)


class DeleteQuestionnaireTypeUseCase(usecases.DeleteUseCase):
    def __init__(self, questionnaire_type: QuestionnaireType):
        super().__init__(questionnaire_type)


class ListQuestionnaireTypeUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._questionnaire_types

    def _factory(self):
        self._questionnaire_types = QuestionnaireType.objects.unarchived()

