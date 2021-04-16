from apps.questionnaire.usecases.questionnaire_usecases import GetQuestionnaireUseCase
from apps.questionnaire.usecases.questionnaire_type_usecases import GetQuestionnaireTypeUseCase


class QuestionnaireTypeMixin:
    def get_questionnaire_type(self, *args, **kwargs):
        return GetQuestionnaireTypeUseCase(
            questionnaire_type_id=self.kwargs.get('questionnaire_type_id')
        ).execute()


class QuestionnaireMixin:
    def get_questionnaire(self, *args, **kwargs):
        return GetQuestionnaireUseCase(
            questionnaire_id=self.kwargs.get('questionnaire_id')
        ).execute()
