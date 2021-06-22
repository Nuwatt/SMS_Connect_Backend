from apps.core.filtersets import IdInFilter
from apps.report.filtersets.base_filtersets import SKUResponseFilter


class SKUCityReportFilter(SKUResponseFilter):
    city = IdInFilter(
        field_name='city',
        label='city',
        lookup_expr='in'
    )
