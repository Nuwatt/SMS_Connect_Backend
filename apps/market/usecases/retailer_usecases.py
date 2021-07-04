import csv

from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from django.http import HttpResponse
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
        self._retailers = Retailer.objects.unarchived().order_by('-created')


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
            retailer, created = Retailer.objects.get_or_create(
                name=item.get('Retailer Name')
            )
            store, created = Store.objects.get_or_create(
                name=item.get('Retailer Branch Name'),
                retailer=retailer,
                channel=channel,
                city=city
            )


class ExportRetailerUseCase(usecases.BaseUseCase):
    columns = ['Retailer Name', 'Retailer Branch Name', 'Channel', 'Country', 'City']

    def execute(self):
        return self._factory()

    def _factory(self):
        response = HttpResponse(content_type='text/csv')
        filename = 'retailer.csv'
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

        # 1. write headers
        writer = csv.writer(response)
        writer.writerow(self.columns)

        # 2. write store
        stores = Store.objects.unarchived().values(
            'name',
            'retailer__name',
            'channel__name',
            'city__country__name',
            'city__name'
        )
        for store in stores:
            writer.writerow([
                store.get('retailer__name'),
                store.get('name'),
                store.get('channel__name'),
                store.get('city__country__name'),
                store.get('city__name')
            ])
        return response
