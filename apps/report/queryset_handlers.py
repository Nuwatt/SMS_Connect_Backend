from dateutil import rrule
from django.db.models import Max, Min, Avg, Count


def sku_min_max_queryset_handler(queryset):
    result = []
    skus = queryset.values(
        'answer__question__sku__name',
    ).distinct()

    for sku in skus:
        sku_answer = queryset.filter(
            answer__question__sku__name=sku.get('answer__question__sku__name')
        )
        statistics = sku_answer.aggregate(
            max=Max('numeric'),
            min=Min('numeric'),
            mean=Avg('numeric'),
        )
        mode = sku_answer.order_by(
            '-frequency'
        ).values('numeric').first()

        result.append({
            'sku': sku.get('answer__question__sku__name'),
            'mode': mode.get('numeric', None),
            'mean': statistics.get('mean'),
            'min': statistics.get('min'),
            'max': statistics.get('max')
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

