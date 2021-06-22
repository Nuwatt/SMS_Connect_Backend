from django.db.models import Count, Q, F
from django.db.models.functions import TruncMonth, ExtractWeek
from django.utils.timezone import now

from apps.core import usecases
from apps.product.models import SKU
from apps.response.models import Response


class SKUOverallReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__question__question_type__name='OOS Question',
            is_completed=True
        ).annotate(
            sku=F('answer__question__sku')
        ).values(
            'sku'
        ).annotate(
            total_answer=Count(
                'answer__choiceanswer__choice',
                filter=Q(answer__question__sku=F('sku'))
            ),
            available=Count(
                'answer__choiceanswer__choice',
                filter=Q(answer__choiceanswer__choice__choice='Available')
            ) / F('total_answer') * 100,
            not_available=Count(
                'answer__choiceanswer__choice',
                filter=Q(answer__choiceanswer__choice__choice='Not Available')
            ) / F('total_answer') * 100,
            less=Count(
                'answer__choiceanswer__choice',
                filter=Q(answer__choiceanswer__choice__choice='Less than six (<6)')
            ) / F('total_answer') * 100,
            sku_name=F('answer__question__sku__name'),
            brand=F('answer__question__sku__brand'),
        ).values(
            'available',
            'not_available',
            'less',
            'sku_name',
            'sku',
            'brand',
        ).unarchived()

        # self._results = SKU.objects.filter(
        #     question__questionnaire__questionnaire_type__name='Out Of Stock',
        #     question__answer__response__is_completed=True
        # ).annotate(
        #     total_answer=Count('question__answer__choiceanswer__choice'),
        #     available=Count(
        #         'question__answer__choiceanswer__choice',
        #         filter=Q(question__answer__choiceanswer__choice__choice='Available')
        #     ) / F('total_answer') * 100,
        #     not_available=Count(
        #         'question__answer__choiceanswer__choice',
        #         filter=Q(question__answer__choiceanswer__choice__choice='Not Available')
        #     ) / F('total_answer') * 100,
        #     less=Count(
        #         'question__answer__choiceanswer__choice',
        #         filter=Q(question__answer__choiceanswer__choice__choice='Less than six (<6)')
        #     ) / F('total_answer') * 100,
        # ).values(
        #     'available',
        #     'name',
        #     'not_available',
        #     'less'
        # ).unarchived()


class SKUMonthAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__question__question_type__name='OOS Question',
            is_completed=True
        ).annotate(
            month=TruncMonth('completed_at')
        ).values(
            'month'
        ).annotate(
            total_answer=Count('answer__choiceanswer__choice'),
            value=Count(
                'answer__choiceanswer__choice',
                filter=Q(answer__choiceanswer__choice__choice='Available')
            ) / F('total_answer') * 100,
            sku_name=F('answer__question__sku__name'),
            sku=F('answer__question__sku'),
            brand=F('answer__question__sku__brand'),
        ).values(
            'value',
            'month',
            'sku_name',
            'sku',
            'brand',
        ).unarchived().filter(
            value__gt=0
        )

        # self._results = SKU.objects.filter(
        #     question__questionnaire__questionnaire_type__name='Out Of Stock',
        #     question__answer__response__is_completed=True
        # ).annotate(
        #     month=TruncMonth('question__answer__response__completed_at'),
        # ).values('name', 'month').annotate(
        #     total_answer=Count('question__answer__choiceanswer__choice'),
        #     value=Count(
        #         'question__answer__choiceanswer__choice',
        #         filter=Q(question__answer__choiceanswer__choice__choice='Available')
        #     ) / F('total_answer') * 100,
        # ).values(
        #     'month',
        #     'value',
        #     'name',
        # ).unarchived().filter(
        #     value__gt=0
        # )


class SKUMonthNotAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__question__question_type__name='OOS Question',
            is_completed=True
        ).annotate(
            month=TruncMonth('completed_at')
        ).values(
            'month'
        ).annotate(
            total_answer=Count('answer__choiceanswer__choice'),
            value=Count(
                'answer__choiceanswer__choice',
                filter=Q(answer__choiceanswer__choice__choice='Not Available')
            ) / F('total_answer') * 100,
            sku_name=F('answer__question__sku__name'),
            sku=F('answer__question__sku'),
            brand=F('answer__question__sku__brand'),
        ).values(
            'value',
            'month',
            'sku_name',
            'sku',
            'brand',
        ).unarchived().filter(
            value__gt=0
        )

        # self._results = SKU.objects.filter(
        #     question__questionnaire__questionnaire_type__name='Out Of Stock',
        #     question__answer__response__is_completed=True
        # ).annotate(
        #     month=TruncMonth('question__answer__response__completed_at'),
        # ).values('name', 'month').annotate(
        #     total_answer=Count('question__answer__choiceanswer__choice'),
        #     value=Count(
        #         'question__answer__choiceanswer__choice',
        #         filter=Q(question__answer__choiceanswer__choice__choice='Not Available')
        #     ) / F('total_answer') * 100,
        # ).values(
        #     'month',
        #     'value',
        #     'name',
        # ).unarchived().filter(
        #     value__gt=0
        # )


class SKUMonthLessReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__question__question_type__name='OOS Question',
            is_completed=True
        ).annotate(
            month=TruncMonth('completed_at')
        ).values(
            'month'
        ).annotate(
            total_answer=Count('answer__choiceanswer__choice'),
            value=Count(
                'answer__choiceanswer__choice',
                filter=Q(answer__choiceanswer__choice__choice='Less than six (<6)')
            ) / F('total_answer') * 100,
            sku_name=F('answer__question__sku__name'),
            sku=F('answer__question__sku'),
            brand=F('answer__question__sku__brand'),
        ).values(
            'value',
            'month',
            'sku_name',
            'sku',
            'brand',
        ).unarchived().filter(
            value__gt=0
        )

        # self._results = SKU.objects.filter(
        #     question__questionnaire__questionnaire_type__name='Out Of Stock',
        #     question__answer__response__is_completed=True
        # ).annotate(
        #     month=TruncMonth('question__answer__response__completed_at'),
        # ).values('name', 'month').annotate(
        #     total_answer=Count('question__answer__choiceanswer__choice'),
        #     value=Count(
        #         'question__answer__choiceanswer__choice',
        #         filter=Q(question__answer__choiceanswer__choice__choice='Less than six (<6)')
        #     ) / F('total_answer') * 100,
        # ).values(
        #     'month',
        #     'value',
        #     'name',
        # ).unarchived().filter(
        #     value__gt=0
        # )


class SKUCityAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__question__question_type__name='OOS Question',
            is_completed=True
        ).annotate(
            city=F('store__city')
        ).values(
            'city'
        ).annotate(
            total_answer=Count('answer__choiceanswer__choice'),
            value=Count(
                'answer__choiceanswer__choice',
                filter=Q(answer__choiceanswer__choice__choice='Available')
            ) / F('total_answer') * 100,
            sku_name=F('answer__question__sku__name'),
            city_name=F('store__city__name'),
            sku=F('answer__question__sku'),
            brand=F('answer__question__sku__brand'),
        ).values(
            'value',
            'city_name',
            'city',
            'sku_name',
            'sku',
            'brand',
        ).unarchived().filter(
            value__gt=0
        )

        # self._results = SKU.objects.filter(
        #     question__questionnaire__questionnaire_type__name='Out Of Stock',
        #     question__answer__response__is_completed=True
        # ).annotate(
        #     city=F('question__answer__response__store__city__name'),
        # ).values('name', 'city').annotate(
        #     total_answer=Count('question__answer__choiceanswer__choice'),
        #     value=Count(
        #         'question__answer__choiceanswer__choice',
        #         filter=Q(question__answer__choiceanswer__choice__choice='Available')
        #     ) / F('total_answer') * 100,
        # ).values(
        #     'city',
        #     'value',
        #     'name',
        # ).unarchived().filter(
        #     value__gt=0
        # )


class SKUCityNotAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__question__question_type__name='OOS Question',
            is_completed=True
        ).annotate(
            city=F('store__city')
        ).values(
            'city'
        ).annotate(
            total_answer=Count('answer__choiceanswer__choice'),
            value=Count(
                'answer__choiceanswer__choice',
                filter=Q(answer__choiceanswer__choice__choice='Not Available')
            ) / F('total_answer') * 100,
            sku_name=F('answer__question__sku__name'),
            city_name=F('store__city__name'),
            sku=F('answer__question__sku'),
            brand=F('answer__question__sku__brand'),
        ).values(
            'value',
            'city_name',
            'city',
            'sku_name',
            'sku',
            'brand',
        ).unarchived().filter(
            value__gt=0
        )

        # self._results = SKU.objects.filter(
        #     question__questionnaire__questionnaire_type__name='Out Of Stock',
        #     question__answer__response__is_completed=True
        # ).annotate(
        #     city=F('question__answer__response__store__city__name'),
        # ).values('name', 'city').annotate(
        #     total_answer=Count('question__answer__choiceanswer__choice'),
        #     value=Count(
        #         'question__answer__choiceanswer__choice',
        #         filter=Q(question__answer__choiceanswer__choice__choice='Not Available')
        #     ) / F('total_answer') * 100,
        # ).values(
        #     'city',
        #     'value',
        #     'name',
        # ).unarchived().filter(
        #     value__gt=0
        # )


class SKUCityLessReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__question__question_type__name='OOS Question',
            is_completed=True
        ).annotate(
            city=F('store__city')
        ).values(
            'city'
        ).annotate(
            total_answer=Count('answer__choiceanswer__choice'),
            value=Count(
                'answer__choiceanswer__choice',
                filter=Q(answer__choiceanswer__choice__choice='Less than six (<6)')
            ) / F('total_answer') * 100,
            sku_name=F('answer__question__sku__name'),
            city_name=F('store__city__name'),
            sku=F('answer__question__sku'),
            brand=F('answer__question__sku__brand'),
        ).values(
            'value',
            'city_name',
            'city',
            'sku_name',
            'sku',
            'brand',
        ).unarchived().filter(
            value__gt=0
        )
        # self._results = SKU.objects.filter(
        #     question__questionnaire__questionnaire_type__name='Out Of Stock',
        #     question__answer__response__is_completed=True
        # ).annotate(
        #     city=F('question__answer__response__store__city__name'),
        # ).values('name', 'city').annotate(
        #     total_answer=Count('question__answer__choiceanswer__choice'),
        #     value=Count(
        #         'question__answer__choiceanswer__choice',
        #         filter=Q(question__answer__choiceanswer__choice__choice='Less than six (<6)')
        #     ) / F('total_answer') * 100,
        # ).values(
        #     'city',
        #     'value',
        #     'name',
        # ).unarchived().filter(
        #     value__gt=0
        # )


class SKUStoreNotAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__question__question_type__name='OOS Question',
            is_completed=True
        ).annotate(
            stores=F('store')
        ).values(
            'stores'
        ).annotate(
            total_answer=Count('answer__choiceanswer__choice'),
            value=Count(
                'answer__choiceanswer__choice',
                filter=Q(answer__choiceanswer__choice__choice='Not Available')
            ) / F('total_answer') * 100,
            sku_name=F('answer__question__sku__name'),
            store_name=F('store__name'),
            sku=F('answer__question__sku'),
            brand=F('answer__question__sku__brand'),
        ).values(
            'value',
            'sku_name',
            'store_name',
            'sku',
            'brand',
        ).unarchived().filter(
            value__gt=0
        )
        # self._results = SKU.objects.filter(
        #     question__questionnaire__questionnaire_type__name='Out Of Stock',
        #     question__answer__response__is_completed=True
        # ).annotate(
        #     store=F('question__answer__response__store__name'),
        # ).values('name', 'store').annotate(
        #     total_answer=Count('question__answer__choiceanswer__choice'),
        #     value=Count(
        #         'question__answer__choiceanswer__choice',
        #         filter=Q(question__answer__choiceanswer__choice__choice='Not Available')
        #     ) / F('total_answer') * 100,
        # ).values(
        #     'store',
        #     'value',
        #     'name',
        # ).unarchived().filter(
        #     value__gt=0
        # )


class SKURetailerLessReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__question__question_type__name='OOS Question',
            is_completed=True
        ).annotate(
            retailer=F('question__answer__response__store__retailer__name'),
        ).values('name', 'retailer').annotate(
            total_answer=Count('question__answer__choiceanswer__choice'),
            value=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Less than six (<6)')
            ) / F('total_answer') * 100,
        ).values(
            'retailer',
            'value',
            'name',
        ).unarchived().filter(
            value__gt=0
        )


class TotalVisitReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__question__question_type__name='OOS Question',
            is_completed=True
        ).annotate(
            city_name=F('store__city__name')
        ).values(
            'city_name'
        ).annotate(
            value=Count(
                'id',
                distinct=True
            )
        ).values('city_name', 'value').filter(value__gt=0).unarchived()

        # self._results = City.objects.annotate(
        #     value=Count(
        #         'store__response',
        #         filter=Q(
        #             store__response__response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
        #         )
        #     ),
        # ).values('name', 'value', ).filter(value__gt=0).unarchived()


class SKUWeekNotAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        current_week = now().isocalendar()[1]
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__question__question_type__name='OOS Question',
            answer__choiceanswer__choice__choice='Not Available',
            is_completed=True
        ).annotate(
            sku=F('answer__question__sku')
        ).values(
            'sku'
        ).annotate(
            completed_week=ExtractWeek('completed_at'),
            week=current_week - F('completed_week'),
            sku_name=F('answer__question__sku__name'),
            brand=F('answer__question__sku__brand'),
        ).values(
            'week',
            'sku_name',
            'sku',
            'brand',
            'store__name',
            'store__retailer__name'
        ).unarchived().filter(week__lte=4)

        # self._results = SKU.objects.filter(
        #     question__questionnaire__questionnaire_type__name='Out Of Stock',
        #     question__answer__response__is_completed=True,
        #     question__answer__choiceanswer__choice__choice='Not Available'
        # ).annotate(
        #     completed_week=ExtractWeek('question__answer__response__completed_at'),
        #     week=current_week - F('completed_week')
        # ).values(
        #     'name',
        #     'week',
        #     'store__name',
        #     'store__retailer__name',
        # ).filter(week__lte=4)
