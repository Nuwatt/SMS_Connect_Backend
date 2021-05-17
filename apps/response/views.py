from apps.core import generics
from apps.questionnaire.mixins import QuestionnaireMixin
from apps.response import serializers, usecases
from apps.user.permissions import IsAgentUser


class StartQuestionnaireView(generics.CreateAPIView, QuestionnaireMixin):
    """
    Use this end-point to start a questionnaire
    """
    serializer_class = serializers.StartQuestionnaireSerializer
    permission_classes = (IsAgentUser,)

    def get_object(self):
        return self.get_questionnaire()

    def perform_create(self, serializer):
        return usecases.StartQuestionnaireUseCase(
            questionnaire=self.get_object(),
            agent_user=self.request.user.agentuser,
            serializer=serializer
        ).execute()
