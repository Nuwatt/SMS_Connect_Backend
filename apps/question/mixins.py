from apps.question.usecases.question_type_usecases import GetQuestionTypeUseCase
from apps.question.usecases.question_usecases import GetQuestionUseCase


class QuestionMixin:
    def get_question(self, *args, **kwargs):
        return GetQuestionUseCase(
            question_id=self.kwargs.get('question_id')
        ).execute()


class QuestionTypeMixin:
    def get_question_type(self, *args, **kwargs):
        return GetQuestionTypeUseCase(
            question_type_id=self.kwargs.get('question_type_id')
        ).execute()
