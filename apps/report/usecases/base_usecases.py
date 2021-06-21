from apps.core import usecases
from apps.questionnaire.models import Questionnaire
from apps.response.models import Response
from apps.user.models import AgentUser


class OverviewReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._result

    def _factory(self):
        self._result = {
            'field_work': AgentUser.objects.unarchived().count(),
            'questionnaire': Questionnaire.objects.unarchived().count(),
            'answer': Response.objects.filter(
                is_archived=False,
                is_completed=True
            ).count(),
        }


