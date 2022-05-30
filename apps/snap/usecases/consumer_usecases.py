import csv
from datetime import datetime

from django.db import IntegrityError
from django.db.models import F, Avg
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.localize.models import Country, City
from apps.question.models import QuestionType
from apps.snap.exceptions import SnapConsumerNotFound
from apps.snap.models import (
    SnapConsumer,
    SnapChannel,
    SnapCategory,
    SnapBrand,
    SnapSKU
)


class GetSnapConsumerUseCase(usecases.BaseUseCase):
    def __init__(self, consumer_snap_id: str):
        self._consumer_snap_id = consumer_snap_id

    def execute(self):
        self._factory()
        return self._consumer_snap

    def _factory(self):
        try:
            self._consumer_snap = SnapConsumer.objects.get(pk=self._consumer_snap_id)
        except SnapConsumer.DoesNotExist:
            raise SnapConsumerNotFound


class ImportSnapConsumerUseCase(usecases.ImportCSVUseCase):
    def __init__(self, serializer):
        super().__init__(serializer)

    valid_columns = [
        'Date', 'Country', 'City', 'Channel', 'Category',
        'Brand', 'SKU', 'Count', 'Question Statement', 'Question Type', 'Total Yes',
        'Total No', 'Rating One On Three', 'Rating Two On Three', 'Rating Three On Three',
        'Rating One On Five', 'Rating Two On Five', 'Rating Three On Five', 'Rating Four On Five',
        'Rating Five On Five', 'Rating One On Ten', 'Rating Two On Ten', 'Rating Three On Ten',
        'Rating Four On Ten', 'Rating Five On Ten', 'Rating Six On Ten',
        'Rating Seven On Ten', 'Rating Eight On Ten', 'Rating Nine On Ten', 'Rating Ten On Ten',
        'Average Numeric'
    ]

    def _factory(self):
        country_data = {}
        city_data = {}
        channel_data = {}
        category_data = {}
        brand_data = {}
        sku_data = {}
        question_type_data = {}

        for item in self._item_list:
            if item.get('Country') not in country_data:
                country, _created = Country.objects.get_or_create(
                    name=item.get('Country'),
                    is_archived=False
                )
                country_data[item.get('Country')] = country

            if item.get('City') not in country_data:
                city, _created = City.objects.get_or_create(
                    name=item.get('City'),
                    country=country_data[item.get('Country')],
                    is_archived=False
                )
                city_data[item.get('City')] = city

            if item.get('Channel') not in channel_data:
                channel, _created = SnapChannel.objects.get_or_create(
                    name=item.get('Channel'),
                    is_archived=False
                )
                channel_data[item.get('Channel')] = channel

            if item.get('Category') not in category_data:
                category, _created = SnapCategory.objects.get_or_create(
                    name=item.get('Category'),
                    is_archived=False
                )
                category_data[item.get('Category')] = category

            if item.get('Brand') not in brand_data:
                brand, _created = SnapBrand.objects.get_or_create(
                    name=item.get('Brand'),
                    is_archived=False
                )
                brand_data[item.get('Brand')] = brand

            if item.get('SKU') not in sku_data:
                sku, _created = SnapSKU.objects.get_or_create(
                    name=item.get('SKU'),
                    brand=brand_data[item.get('Brand')],
                    category=category_data[item.get('Category')],
                    is_archived=False
                )
                sku.country.add(country_data[item.get('Country')])
                sku_data[item.get('SKU')] = sku

            if item.get('Question Type') not in sku_data:
                question_type = QuestionType.objects.get(
                    name=item.get('Question Type'),
                )
                question_type_data[item.get('Question Type')] = question_type

            snap, _created = SnapConsumer.objects.update_or_create(
                country_id=country_data[item.get('Country')].id,
                country_name=country_data[item.get('Country')].name,
                city_id=city_data[item.get('City')].id,
                city_name=city_data[item.get('City')].name,
                channel_id=channel_data[item.get('Channel')].id,
                channel_name=channel_data[item.get('Channel')].name,
                category_id=category_data[item.get('Category')].id,
                category_name=category_data[item.get('Category')].name,
                brand_id=brand_data[item.get('Brand')].id,
                brand_name=brand_data[item.get('Brand')].name,
                sku_id=sku_data[item.get('SKU')].id,
                sku_name=sku_data[item.get('SKU')].name,
                date=datetime.strptime(item.get('Date'), "%Y-%m-%d").date(),
                defaults={
                    'count': item.get('Count'),
                    'question_statement': item.get('Question Statement'),
                    'question_type': question_type_data[item.get('Question Type')],
                    'total_yes': item.get('Total Yes'),
                    'total_no': item.get('Total No'),
                    'rating_one_on_three': item.get('Rating One On Three'),
                    'rating_two_on_three': item.get('Rating Two On Three'),
                    'rating_three_on_three': item.get('Rating Three On Three'),
                    'rating_one_on_five': item.get('Rating One On Five'),
                    'rating_two_on_five': item.get('Rating Two On Five'),
                    'rating_three_on_five': item.get('Rating Three On Five'),
                    'rating_four_on_five': item.get('Rating Four On Five'),
                    'rating_five_on_five': item.get('Rating Five On Five'),
                    'rating_one_on_ten': item.get('Rating One On Ten'),
                    'rating_two_on_ten': item.get('Rating Two On Ten'),
                    'rating_three_on_ten': item.get('Rating Three On Ten'),
                    'rating_four_on_ten': item.get('Rating Four On Ten'),
                    'rating_five_on_ten': item.get('Rating Five On Ten'),
                    'rating_six_on_ten': item.get('Rating Six On Ten'),
                    'rating_seven_on_ten': item.get('Rating Seven On Ten'),
                    'rating_eight_on_ten': item.get('Rating Eight On Ten'),
                    'rating_nine_on_ten': item.get('Rating Nine On Ten'),
                    'rating_ten_on_ten': item.get('Rating Ten On Ten'),
                    'average_numeric': item.get('Average Numeric')
                }
            )

    def execute(self):
        self.is_valid()
        try:
            self._factory()
        except IntegrityError as e:
            print(e)
            raise ValidationError({
                'non_field_errors': _('CSV Contains invalid ids.')
            })


class ListSnapConsumerUseCase(usecases.BaseUseCase):
    def execute(self):
        return self._factory()

    def _factory(self):
        return SnapConsumer.objects.values(
            'id', 'created', 'city__name', 'channel__name', 'city__country__name',
            'city__country__name', 'sku__category__name', 'sku__brand__name',
            'sku__name', 'question_type__name', 'date',
            'count', 'question_statement', 'total_yes',
            'total_no', 'rating_one_on_three', 'rating_two_on_three', 'rating_three_on_three',
            'rating_one_on_five', 'rating_two_on_five', 'rating_three_on_five', 'rating_four_on_five',
            'rating_five_on_five', 'rating_one_on_ten', 'rating_two_on_ten', 'rating_three_on_ten',
            'rating_four_on_ten', 'rating_five_on_ten', 'rating_six_on_ten', 'rating_seven_on_ten',
            'rating_eight_on_ten', 'rating_nine_on_ten', 'rating_ten_on_ten', 'average_numeric'
        ).unarchived()


class DeleteSnapConsumerUseCase(usecases.DeleteUseCase):
    def __init__(self, consumer_snap: SnapConsumer):
        super().__init__(consumer_snap)


class UpdateSnapConsumerUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, consumer_snap: SnapConsumer):
        super().__init__(serializer, consumer_snap)


class YesNoQuestionSnapConsumerUseCase(usecases.BaseUseCase):

    def _factory(self):
        return SnapConsumer.objects.filter(
            question_type__name='Yes or No'
        ).annotate(
            yes=F('total_yes'),
            no=F('total_no')
        ).values(
            'question_statement',
            'yes',
            'no'
        ).unarchived()


class RatingOneToThreeSnapConsumerUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapConsumer.objects.filter(
            question_type__name='Rating 1 to 3',
            is_archived=False
        )


class RatingOneToFiveSnapConsumerUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapConsumer.objects.filter(
            question_type__name='Rating 1 to 5',
            is_archived=False
        )


class RatingOneToTenSnapConsumerUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapConsumer.objects.filter(
            question_type__name='Rating 1 to 10',
            is_archived=False
        )


class NumericAverageSnapConsumerUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapConsumer.objects.filter(
            question_type__name='Numeric',
            is_archived=False
        ).values(
            'question_statement'
        ).distinct().annotate(
            value=Avg('average_numeric')
        ).values(
            'question_statement',
            'value'
        )


class BulkDeleteSnapConsumerUseCase(usecases.CreateUseCase):
    def _factory(self):
        SnapConsumer.objects.filter(
            is_archived=False,
            id__in=self._data.get('snap_ids')
        ).archive()


class ExportSnapConsumerUseCase(usecases.BaseUseCase):
    def __init__(self, filter_backends, request, view_self):
        self._view_self = view_self
        self._request = request
        self._filter_backends = filter_backends

    columns = [
        'Date', 'Country', 'City', 'Channel', 'Category',
        'Brand', 'SKU', 'Count', 'Question Statement', 'Question Type', 'Total Yes',
        'Total No', 'Rating One On Three', 'Rating Two On Three', 'Rating Three On Three',
        'Rating One On Five', 'Rating Two On Five', 'Rating Three On Five', 'Rating Four On Five',
        'Rating Five On Five', 'Rating One On Ten', 'Rating Two On Ten', 'Rating Three On Ten',
        'Rating Four On Ten', 'Rating Five On Ten', 'Rating Six On Ten',
        'Rating Seven On Ten', 'Rating Eight On Ten', 'Rating Nine On Ten', 'Rating Ten On Ten',
        'Average Numeric'
    ]

    def _factory(self):
        response = HttpResponse(content_type='text/csv')
        filename = 'consumer_snap.csv'
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

        # 1. write headers
        writer = csv.writer(response)
        writer.writerow(self.columns)

        # 2. write questions
        queryset = SnapConsumer.objects.unarchived().values(
            'date', 'country_name', 'city_name', 'channel_name', 'category_name',
            'brand_name', 'sku_name', 'count', 'question_statement', 'question_type__name', 'total_yes',
            'total_no', 'rating_one_on_three', 'rating_two_on_three', 'rating_three_on_three',
            'rating_one_on_five', 'rating_two_on_five', 'rating_three_on_five', 'rating_four_on_five',
            'rating_five_on_five', 'rating_one_on_ten', 'rating_two_on_ten', 'rating_three_on_ten',
            'rating_four_on_ten', 'rating_five_on_ten', 'rating_six_on_ten', 'rating_seven_on_ten',
            'rating_eight_on_ten', 'rating_nine_on_ten', 'rating_ten_on_ten', 'average_numeric'
        )
        snaps = None
        for backend in list(self._filter_backends):
            snaps = backend().filter_queryset(self._request, queryset, self._view_self)

        for snap in snaps:
            writer.writerow([
                *snap.values()
            ])
        return response
