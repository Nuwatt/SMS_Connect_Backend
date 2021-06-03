from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.core.validators import validate_non_zero_integer
from apps.questionnaire.models import Questionnaire


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'


class AddQuestionnaireSerializer(QuestionnaireSerializer):
    repeat_cycle = serializers.IntegerField(required=False, validators=[validate_non_zero_integer])

    class Meta(QuestionnaireSerializer.Meta):
        fields = (
            'name',
            'questionnaire_type',
            'repeat_cycle',
            'city',
            'tags',
            'category'
        )
        extra_kwargs = {
            'category': {
                'required': True
            }
        }


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


class ListAvailableQuestionnaireForAgentSerializer(QuestionnaireSerializer):
    number_of_questions = serializers.IntegerField()
    initiated_data = serializers.DateTimeField(source='created', format='%d-%m-%Y')
    questionnaire_type = serializers.CharField()

    class Meta(QuestionnaireSerializer.Meta):
        fields = (
            'id',
            'name',
            'questionnaire_type',
            'initiated_data',
            'number_of_questions'
        )
