from apps.question.usecases.question_usecases import GetQuestionUseCase


class QuestionMixin:
    def get_question(self, *args, **kwargs):
        return GetQuestionUseCase(
            question_id=self.kwargs.get('question_id')
        ).execute()
