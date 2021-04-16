from rest_framework import serializers

from apps.questionnaire.models import Questionnaire


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'


class AddQuestionnaireSerializer(QuestionnaireSerializer):
    class Meta(QuestionnaireSerializer.Meta):
        fields = (
            'name',
            'questionnaire_type',
            'city',
            'area',
            'country'
        )


class ListQuestionnaireSerializer(AddQuestionnaireSerializer):
    class Meta(AddQuestionnaireSerializer.Meta):
        fields = (
            'id',
        ) + AddQuestionnaireSerializer.Meta.fields


class UpdateQuestionnaireSerializer(AddQuestionnaireSerializer):
    pass
