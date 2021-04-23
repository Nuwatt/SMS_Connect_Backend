from apps.terms_and_conditions.usecases import GetTermsAndConditionsUseCase


class TermsAndConditionsMixin:
    def get_terms_and_conditions(self, *args, **kwargs):
        return GetTermsAndConditionsUseCase().execute()


