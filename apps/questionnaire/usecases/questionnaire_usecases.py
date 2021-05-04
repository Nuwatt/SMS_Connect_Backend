from apps.questionnaire.exceptions import QuestionnaireNotFound
from apps.core import usecases
from apps.questionnaire.models import Questionnaire


class GetQuestionnaireUseCase(usecases.BaseUseCase):
    def __init__(self, questionnaire_id: str):
        self._questionnaire_id = questionnaire_id

    def execute(self):
        self._factory()
        return self._questionnaire

    def _factory(self):
        try:
            self._questionnaire = Questionnaire.objects.get(pk=self._questionnaire_id)
        except Questionnaire.DoesNotExist:
            raise QuestionnaireNotFound


class AddQuestionnaireUseCase(usecases.CreateUseCase):

    def execute(self):
        self._factory()
        return self._questionnaire

    def _factory(self):
        # 1. pop city and country and tags
        city = self._data.pop('city')
        country = self._data.pop('country')
        tags = self._data.pop('tags')

        # 2. create questionnaire
        self._questionnaire = Questionnaire.objects.create(**self._data)

        # 3. set city and country and tags
        self._questionnaire.city.set(city)
        self._questionnaire.country.set(country)
        self._questionnaire.tags.set(tags)


class UpdateQuestionnaireUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, questionnaire: Questionnaire):
        super().__init__(serializer, questionnaire)


class DeleteQuestionnaireUseCase(usecases.DeleteUseCase):
    def __init__(self, questionnaire: Questionnaire):
        super().__init__(questionnaire)


class ListQuestionnaireUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._questionnaires

    def _factory(self):
        self._questionnaires = Questionnaire.objects.unarchived()
