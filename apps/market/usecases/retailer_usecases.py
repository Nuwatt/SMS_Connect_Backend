from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from rest_framework.exceptions import ValidationError

from apps.localize.models import Country, City
from apps.market.exceptions import RetailerNotFound
from apps.market.models import Retailer, Channel, Store
from apps.core import usecases
from apps.user.models import AgentUser


class GetRetailerUseCase(usecases.BaseUseCase):
    def __init__(self, retailer_id: str):
        self._retailer_id = retailer_id

    def execute(self):
        self._factory()
        return self._retailer

    def _factory(self):
        try:
            self._retailer = Retailer.objects.get(pk=self._retailer_id)
        except Retailer.DoesNotExist:
            raise RetailerNotFound


class AddRetailerUseCase(usecases.CreateUseCase):
    def _factory(self):
        retailers = []
        for name in self._data.get('name'):
            retailer = Retailer(
                name=name,
                channel=self._data.get('channel')
            )
            try:
                retailer.full_clean()
            except DjangoValidationError as e:
                raise ValidationError(e.message_dict)
            retailers.append(retailer)
        Retailer.objects.bulk_create(retailers)


class UpdateRetailerUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, retailer: Retailer):
        super().__init__(serializer, retailer)


class DeleteRetailerUseCase(usecases.DeleteUseCase):
    def __init__(self, retailer: Retailer):
        super().__init__(retailer)


class ListRetailerUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._retailers

    def _factory(self):
        self._retailers = Retailer.objects.unarchived().select_related(
            'channel'
        )


class BasicListRetailerUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._retailers

    def _factory(self):
        self._retailers = Retailer.objects.unarchived()


class ListRetailerForAgentUserUseCase(usecases.BaseUseCase):
    def __init__(self, agent_user: AgentUser):
        self._agent_user = agent_user

    def execute(self):
        self._factory()
        return self._retailers

    def _factory(self):
        self._retailers = Retailer.objects.filter(
            store__city__in=self._agent_user.operation_city.all()
        ).unarchived()


class ImportRetailerUseCase(usecases.ImportCSVUseCase):
    valid_columns = ['Retailer Name', 'Retailer Branch Name', 'Channel', 'Country', 'City']

    @transaction.atomic
    def _factory(self):
        for item in self._item_list:
            country, created = Country.objects.get_or_create(name=item.get('Country'))
            city, created = City.objects.get_or_create(name=item.get('City'), country=country)
            channel, created = Channel.objects.get_or_create(name=item.get('Channel'))
            retailer, created = Retailer.objects.update_or_create(
                name=item.get('Retailer Name'),
                defaults={
                    'channel': channel,
                }
            )
            store, created = Store.objects.get_or_create(
                name=item.get('Retailer Branch Name'),
                retailer=retailer,
                channel=channel,
                city=city
            )
