from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny

from apps.core import generics
from apps.snap import filtersets
from apps.snap.serializers import filters_serializers
from apps.snap.usecases import filters_usecases


class BaseFiltersView(generics.ListAPIView):
    pagination_class = None
    permission_classes = (AllowAny,)

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
        else:
            raise ValidationError({
                'questionnaire_type': _('This filter params is required.')
            })


class ListSKUFiltersView(BaseFiltersView):
    """
    Use this end-point to list SKU filters
    """
    serializer_class = filters_serializers.ListSKUFiltersSerializer

    def get_queryset(self):
        self.set_filterset_class()
        if self.questionnaire_type == '7':
            return filters_usecases.ListSKUFiltersUseCase().execute()


class ListBrandFiltersView(BaseFiltersView):
    """
    Use this end-point to list Brand filters
    """
    serializer_class = filters_serializers.ListBrandFiltersSerializer

    def get_queryset(self):
        self.set_filterset_class()
        if self.questionnaire_type == '7':
            return filters_usecases.ListBrandFiltersUseCase().execute()


class ListCategoryFiltersView(BaseFiltersView):
    """
    Use this end-point to list category filters
    """
    serializer_class = filters_serializers.ListCategoryFiltersSerializer

    def get_queryset(self):
        self.set_filterset_class()
        if self.questionnaire_type == '7':
            return filters_usecases.ListCategoryFiltersUseCase().execute()


class ListCityFiltersView(BaseFiltersView):
    """
    Use this end-point to list city filters
    """
    serializer_class = filters_serializers.ListCityFiltersSerializer

    def get_queryset(self):
        self.set_filterset_class()
        if self.questionnaire_type == '7':
            return filters_usecases.ListCityFiltersUseCase().execute()


class ListCountryFiltersView(BaseFiltersView):
    """
    Use this end-point to list Country filters
    """
    serializer_class = filters_serializers.ListCountryFiltersSerializer

    def get_queryset(self):
        self.set_filterset_class()
        if self.questionnaire_type == '7':
            return filters_usecases.ListCountryFiltersUseCase().execute()


class ListChannelFiltersView(BaseFiltersView):
    """
    Use this end-point to list Channel filters
    """
    serializer_class = filters_serializers.ListChannelFiltersSerializer

    def get_queryset(self):
        self.set_filterset_class()
        if self.questionnaire_type == '7':
            return filters_usecases.ListChannelFiltersUseCase().execute()
