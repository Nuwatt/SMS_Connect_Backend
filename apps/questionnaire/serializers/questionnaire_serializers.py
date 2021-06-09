from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from apps.core.serializers import IdNameSerializer, IdNameCharSerializer
from apps.core.validators import validate_non_zero_integer
from apps.questionnaire.models import Questionnaire
from apps.user.serializers.agent_user_serializers import BasicListAgentUserSerializer


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
    country = serializers.SerializerMethodField()
    city = IdNameSerializer(many=True)
    category = IdNameCharSerializer()
    repeat_cycle = serializers.SerializerMethodField()

    class Meta(AddQuestionnaireSerializer.Meta):
        fields = AddQuestionnaireSerializer.Meta.fields + (
            'id',
            'country',
        )

    @swagger_serializer_method(serializer_or_field=serializers.ListSerializer(child=serializers.CharField()))
    def get_country(self, instance):
        countries = [{
            'id': item.country.id,
            'name': item.country.name
        } for item in instance.city.all()]
        return IdNameSerializer(countries, many=True).data

    @swagger_serializer_method(serializer_or_field=serializers.IntegerField())
    def get_repeat_cycle(self, instance):
        if instance.repeat_cycle:
            weeks = instance.repeat_cycle.days / 7
            if weeks:
                return weeks
        return None


class ListQuestionnaireSerializer(QuestionnaireDetailSerializer):
    number_of_questions = serializers.IntegerField()
    initiated_data = serializers.DateTimeField(source='created', format='%d-%m-%Y')
    questionnaire_type = serializers.CharField()
    tags = BasicListAgentUserSerializer(many=True)

    class Meta(QuestionnaireDetailSerializer.Meta):
        fields = QuestionnaireDetailSerializer.Meta.fields + (
            'initiated_data',
            'number_of_questions',
            'country',
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
