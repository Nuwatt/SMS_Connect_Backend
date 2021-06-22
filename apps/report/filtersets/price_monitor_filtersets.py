from apps.core.filtersets import IdInFilter
from apps.report.filtersets.base_filtersets import ResponseFilter, SKUResponseFilter


class BrandMinMaxReportFilter(ResponseFilter):
    brand = IdInFilter(
        field_name='brand',
        label='brand',
        lookup_expr='in'
    )
