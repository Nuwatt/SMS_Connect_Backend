from rest_framework import serializers

from apps.questionnaire.models import QuestionnaireType


class QuestionnaireTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireType
        fields = '__all__'


class AddQuestionnaireTypeSerializer(QuestionnaireTypeSerializer):
    class Meta(QuestionnaireTypeSerializer.Meta):
        fields = (
            'name',
        )


class ListQuestionnaireTypeSerializer(QuestionnaireTypeSerializer):
    class Meta(QuestionnaireTypeSerializer.Meta):
        fields = (
            'id',
            'name',
        )


class UpdateQuestionnaireTypeSerializer(AddQuestionnaireTypeSerializer):
    pass
