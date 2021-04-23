from rest_framework import serializers

from apps.terms_and_conditions.models import TermsAndConditions


class TermsAndConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsAndConditions
        fields = '__all__'


class AddTermsAndConditionsSerializer(TermsAndConditionsSerializer):
    class Meta(TermsAndConditionsSerializer.Meta):
        fields = (
            'text',
        )


class TermsAndConditionsDetailSerializer(AddTermsAndConditionsSerializer):
    pass


class UpdateTermsAndConditionsSerializer(AddTermsAndConditionsSerializer):
    pass
