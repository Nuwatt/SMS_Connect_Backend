from apps.core import usecases
from apps.localize.exceptions import CountryNotFound
from apps.localize.models import Country
from apps.user.models import AgentUser


class GetCountryUseCase(usecases.BaseUseCase):
    def __init__(self, country_id: str):
        self._country_id = country_id

    def execute(self):
        self._factory()
        return self._country

    def _factory(self):
        try:
            self._country = Country.objects.get(pk=self._country_id)
        except Country.DoesNotExist:
            raise CountryNotFound


class AddCountryUseCase(usecases.CreateUseCase):
    def _factory(self):
        Country.objects.create(**self._data)


class UpdateCountryUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, country: Country):
        super().__init__(serializer, country)


class DeleteCountryUseCase(usecases.DeleteUseCase):
    def __init__(self, country: Country):
        super().__init__(country)


class ListCountryUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._countries

    def _factory(self):
        self._countries = Country.objects.unarchived()


class ListCountryForAgentUserUseCase(usecases.BaseUseCase):
    def __init__(self, agent_user: AgentUser):
        self._agent_user = agent_user

    def execute(self):
        self._factory()
        return self._countries

    def _factory(self):
        self._countries = self._agent_user.operation_country.all()

