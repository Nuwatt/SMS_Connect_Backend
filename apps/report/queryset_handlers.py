from django.db.models import Max, Min, Avg, Count


def sku_min_max_queryset_handler(queryset):
    result = []
    skus = queryset.values(
        'answer__question__sku__name',
    ).distinct()

    for index, sku in enumerate(skus):
        print(sku)
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
            'mode': mode.get('numeric'),
            'mean': statistics.get('mean'),
            'min': statistics.get('min'),
            'max': statistics.get('max')
        })
        print('-'*100)
    return result
