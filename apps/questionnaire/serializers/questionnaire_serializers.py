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
            'category',
            'country',
            'tags'
        )


class QuestionnaireDetailSerializer(QuestionnaireSerializer):
    class Meta(AddQuestionnaireSerializer.Meta):
        fields = (
            'id',
        ) + AddQuestionnaireSerializer.Meta.fields


class ListQuestionnaireSerializer(QuestionnaireDetailSerializer):
    number_of_questions = serializers.IntegerField()
    initiated_data = serializers.DateTimeField(source='created', format='%d-%m-%Y')
    questionnaire_type = serializers.CharField()
    country = serializers.ListSerializer(child=serializers.CharField())
    city = serializers.ListSerializer(child=serializers.CharField())
    tags = serializers.ListSerializer(child=serializers.CharField())

    class Meta(QuestionnaireDetailSerializer.Meta):
        fields = QuestionnaireDetailSerializer.Meta.fields + (
            'initiated_data',
            'number_of_questions',
        )


class UpdateQuestionnaireSerializer(AddQuestionnaireSerializer):
    pass
