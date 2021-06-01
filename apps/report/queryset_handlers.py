from dateutil import rrule
from django.db import models
from django.db.models import Max, Min, Avg, Count, OuterRef, Subquery, F, Value
from django_mysql.models import GroupConcat
from sql_util.aggregates import SubqueryCount, SubqueryMax

from apps.response.models import Answer, NumericAnswer


def sku_min_max_queryset_handler(queryset):
    numeric_answer = Answer.objects.filter(
        question__sku=OuterRef('pk'),
        response__retailer=OuterRef('question__answer__response__retailer')
    ).annotate(
        frequency=Count('numericanswer__numeric')
    ).order_by(
        '-frequency'
    ).values('numericanswer__numeric')[:1]

    return queryset.annotate(
        max=Max('question__answer__numericanswer__numeric'),
        min=Min('question__answer__numericanswer__numeric'),
        mean=Avg('question__answer__numericanswer__numeric'),
        mode=Subquery(numeric_answer)
    )
    # for sku in queryset:

    # questions = sku.question_set.all()
    # for question in questions:
    #     answers = question.answer_set.select_related(
    #         'numeric'
    #     ).values('numericanswer__numeric')
    #     print(answers)
    #     # statistics = answers.aggregate(
    #     #     max=Max('numericanswer__numeric'),
    #     #     min=Min('numericanswer__numeric'),
    #     #     mean=Avg('numericanswer__numeric'),
    #     # )
    #     # result.append({
    #     #         'sku': sku.name,
    #     #         'mode': None,
    #     #         'mean': statistics.get('mean'),
    #     #         'min': statistics.get('min'),
    #     #         'max': statistics.get('max')
    #     #     })

    # skus = queryset.values(
    #     'answer__question__sku__name',
    # ).distinct()
    #
    # for sku in skus:
    #     sku_answer = queryset.filter(
    #         answer__question__sku__name=sku.get('answer__question__sku__name')
    #     )
    #     statistics = sku_answer.aggregate(
    #         max=Max('numeric'),
    #         min=Min('numeric'),
    #         mean=Avg('numeric'),
    #     )
    #     mode = sku_answer.order_by(
    #         '-frequency'
    #     ).values('numeric').first()
    #
    #     result.append({
    #         'sku': sku.get('answer__question__sku__name'),
    #         'mode': mode.get('numeric', None),
    #         'mean': statistics.get('mean'),
    #         'min': statistics.get('min'),
    #         'max': statistics.get('max')
    #     })
    # return result


def answer_per_county_handler(queryset):
    result = []
    skus = queryset.values(
        'answer__question__sku__name',
    ).distinct()

    countries = queryset.values(
        'answer__response__retailer__country__name'
    ).distinct()

    for sku in skus:
        sku_answer = queryset.filter(
            answer__question__sku__name=sku.get('answer__question__sku__name')
        )
        country_result = []
        for country in countries:
            statistics = sku_answer.filter(
                answer__response__retailer__country__name=country.get('answer__response__retailer__country__name')
            )
            country_result.append({
                'country': country.get('answer__response__retailer__country__name'),
                'value': len(statistics)
            })
        result.append({
            'sku': sku.get('answer__question__sku__name'),
            'statistics': country_result
        })

    return result


def answer_per_city_handler(queryset):
    result = []
    skus = queryset.values(
        'answer__question__sku__name',
    ).distinct()

    cities = queryset.values(
        'answer__response__retailer__city__name'
    ).distinct()

    for sku in skus:
        sku_answer = queryset.filter(
            answer__question__sku__name=sku.get('answer__question__sku__name')
        )
        city_result = []
        for city in cities:
            statistics = sku_answer.filter(
                answer__response__retailer__city__name=city.get('answer__response__retailer__city__name')
            )
            city_result.append({
                'city': city.get('answer__response__retailer__city__name'),
                'value': len(statistics)
            })
        result.append({
            'sku': sku.get('answer__question__sku__name'),
            'statistics': city_result
        })

    return result


class SKUQuerysetHandler:
    result = []

    def __init__(self, queryset):
        self.queryset = queryset

    def handler(self, func):
        return self.result

    def max(self):
        return self.handler(func=self._compute_max)

    def min(self):
        return self.handler(func=self._compute_min)

    def mean(self):
        return self.handler(func=self._compute_mean)

    def mode(self):
        return self.handler(func=self._compute_mode)

    def _compute_max(self, sku_answer):
        return sku_answer.aggregate(
            max=Max('numeric'),
        ).get('max')

    def _compute_min(self, sku_answer):
        return sku_answer.aggregate(
            min=Min('numeric'),
        ).get('min')

    def _compute_mean(self, sku_answer):
        return sku_answer.aggregate(
            mean=Avg('numeric'),
        ).get('mean')

    def _compute_mode(self, sku_answer):
        return sku_answer.annotate(
            frequency=Count('numeric')
        ).order_by(
            '-frequency'
        ).values('numeric').first().get('numeric')


class SKUCountryQuerysetHandler(SKUQuerysetHandler):
    def handler(self, func):
        skus = self.queryset.values(
            'answer__question__sku__name',
        ).distinct()

        countries = self.queryset.values(
            'answer__response__retailer__country__name'
        ).distinct()

        for sku in skus:
            month_result = []
            for country in countries:
                sku_answer = self.queryset.filter(
                    answer__question__sku__name=sku.get('answer__question__sku__name'),
                    answer__response__retailer__country__name=country.get('answer__response__retailer__country__name'),
                )

                month_result.append({
                    'country': country.get('answer__response__retailer__country__name'),
                    'value': func(sku_answer)
                })

            self.result.append({
                'sku': sku.get('answer__question__sku__name'),
                'statistics': month_result
            })
        return self.result


class SKUMonthQuerysetHandler(SKUQuerysetHandler):
    def handler(self, func):
        skus = self.queryset.values(
            'answer__question__sku__name',
        ).distinct()

        for sku in skus:
            date_range = self.queryset.aggregate(
                max=Max('answer__response__completed_at'),
                min=Min('answer__response__completed_at'),
            )
            month_result = []
            for dt in rrule.rrule(rrule.MONTHLY, dtstart=date_range.get('min'), until=date_range.get('max')):
                sku_answer = self.queryset.filter(
                    answer__question__sku__name=sku.get('answer__question__sku__name'),
                    answer__response__completed_at__month=dt.month,
                )
                month_result.append({
                    'date_time': dt,
                    'value': func(sku_answer)
                })

            self.result.append({
                'sku': sku.get('answer__question__sku__name'),
                'statistics': month_result
            })
        return self.result


def sku_mon_max_handler(queryset):
    result = []
    # skus = queryset.values('name')
    answer = queryset.annotate(
        date=F('question__answer__response__completed_at'),
        value=Max('question__answer__numericanswer__numeric')
    ).values('date', 'value')

    # for item in answer:
    #     print(item.value, item.date)
    for sku in answer:
        print(sku.get('value'), sku.get('date').strftime('%b'))

        # for dt in rrule.rrule(rrule.MONTHLY, dtstart=date_range.get('min'), until=date_range.get('max')):
        #     print(answer[0].get('value'))
    #     #     statistics.append({
    #     #         'date': dt,
    #     #         'value': answer.get('max')
    #     #     })
    #     # result.append({
    #     #     'name': sku,
    #     #     'statistics': statistics
    #     # })
    return result
    # print(len(queryset))
    # numeric_answer = Answer.objects.filter(
    #     question__sku=OuterRef('pk'),
    #     response__retailer=OuterRef('question__answer__response__retailer')
    # ).values('numericanswer__numeric', 'response__completed_at')
    #
    # a = queryset.annotate(
    #     statistics=GroupConcat(numeric_answer)
    # )
    # for i in a:
    #     print(i.statistics)
    # return a
