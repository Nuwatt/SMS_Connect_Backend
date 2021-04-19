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
    def _factory(self):
        # 1. pop city and country
        city = self._data.pop('city')
        country = self._data.pop('country')

        # 2. create questionnaire
        questionnaire = Questionnaire.objects.create(**self._data)

        # 3. set city and country
        questionnaire.city.set(city)
        questionnaire.country.set(country)


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
