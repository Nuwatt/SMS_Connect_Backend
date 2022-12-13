from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny

from apps.core import generics
from apps.snap import filtersets
from apps.snap.models import SnapPriceMonitor, SnapDistribution, SnapOutOfStock
from apps.snap.serializers import filters_serializers
from apps.snap.usecases import filters_usecases


class BaseFiltersView(generics.ListAPIView):
    pagination_class = None
    permission_classes = (AllowAny,)
    snap_model = None

    def set_filterset_class(self):
        # model = {
        #     '2': 'Consumer',
        #     '3': 'OOS',
        #     '4': 'DC',
        #     '7': 'PM',
        # }
        self.questionnaire_type = self.request.GET.get('questionnaire_type', None)
        if self.questionnaire_type == '7':
            self.filterset_class = filtersets.SnapPriceMonitorFilter
        elif self.questionnaire_type == '4':
            self.filterset_class = filtersets.SnapDistributionFilter
        elif self.questionnaire_type == '3':
            self.filterset_class = filtersets.SnapOutOfStockFilter
        else:
            raise ValidationError({
                'questionnaire_type': _('This filter params is required.')
            })

    def get_snap_model(self):
        self.questionnaire_type = self.request.GET.get('questionnaire_type', None)
        if self.questionnaire_type == '7':
            self.snap_model = SnapPriceMonitor
        elif self.questionnaire_type == '4':
            self.snap_model = SnapDistribution
        elif self.questionnaire_type == '3':
            self.snap_model = SnapOutOfStock
        else:
            raise ValidationError({
                'questionnaire_type': _('This filter params is required.')
            })

    def get_queryset(self):
        self.set_filterset_class()
        self.get_snap_model()


class ListSKUFiltersView(BaseFiltersView):
    """
    Use this end-point to list SKU filters
    """
    serializer_class = filters_serializers.ListSKUFiltersSerializer

    def get_queryset(self):
        super(ListSKUFiltersView, self).get_queryset()
        return filters_usecases.ListSKUFiltersUseCase(
            snap_model=self.snap_model
        ).execute()


class ListBrandFiltersView(BaseFiltersView):
    """
    Use this end-point to list Brand filters
    """
    serializer_class = filters_serializers.ListBrandFiltersSerializer

    def get_queryset(self):
        super(ListBrandFiltersView, self).get_queryset()
        return filters_usecases.ListBrandFiltersUseCase(
            snap_model=self.snap_model
        ).execute()


class ListCategoryFiltersView(BaseFiltersView):
    """
    Use this end-point to list category filters
    """
    serializer_class = filters_serializers.ListCategoryFiltersSerializer

    def get_queryset(self):
        super(ListCategoryFiltersView, self).get_queryset()
        return filters_usecases.ListCategoryFiltersUseCase(
            snap_model=self.snap_model
        ).execute()


class ListCityFiltersView(BaseFiltersView):
    """
    Use this end-point to list city filters
    """
    serializer_class = filters_serializers.ListCityFiltersSerializer

    def get_queryset(self):
        super(ListCityFiltersView, self).get_queryset()
        return filters_usecases.ListCityFiltersUseCase(
            snap_model=self.snap_model
        ).execute()


class ListCountryFiltersView(BaseFiltersView):
    """
    Use this end-point to list Country filters
    """
    serializer_class = filters_serializers.ListCountryFiltersSerializer

    def get_queryset(self):
        super(ListCountryFiltersView, self).get_queryset()
        return filters_usecases.ListCountryFiltersUseCase(
            snap_model=self.snap_model
        ).execute()


class ListChannelFiltersView(BaseFiltersView):
    """
    Use this end-point to list Channel filters
    """
    serializer_class = filters_serializers.ListChannelFiltersSerializer

    def get_queryset(self):
        super(ListChannelFiltersView, self).get_queryset()
        return filters_usecases.ListChannelFiltersUseCase(
            snap_model=self.snap_model
        ).execute()

