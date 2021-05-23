from django.utils.translation import gettext_lazy as _

from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.core.serializers import IdNameSerializer, CSVFileInputSerializer
from apps.question.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AddQuestionSerializer(QuestionSerializer):
    question_options = serializers.ListSerializer(
        child=serializers.CharField(),
        required=False
    )

    class Meta(QuestionSerializer.Meta):
        fields = (
            'question_type',
            'statement',
            'question_options',
            'brand',
            'sku',
        )

    def validate(self, attrs):
        # 1. if question_type has_options then it is required
        if attrs.get('question_type').has_options and not attrs.get('question_options', None):
            raise ValidationError({
                'question_options': _('This field is required.')
            })
        return attrs


class ListQuestionSerializer(AddQuestionSerializer):
    question_options = serializers.SerializerMethodField()
    brand = IdNameSerializer()
    sku = IdNameSerializer()

    class Meta(AddQuestionSerializer.Meta):
        fields = (
                     'id',
                 ) + AddQuestionSerializer.Meta.fields

    @swagger_serializer_method(serializer_or_field=serializers.ListSerializer(child=serializers.CharField()))
    def get_question_options(self, instance):
        return instance.questionoption_set.values_list('option', flat=True)


class ListQuestionForAgentUserSerializer(QuestionSerializer):
    question_options = serializers.SerializerMethodField()
    question_type = serializers.CharField()

    class Meta(QuestionSerializer.Meta):
        fields = (
            'id',
            'statement',
            'question_type',
            'question_options',
        )

    @swagger_serializer_method(serializer_or_field=IdNameSerializer())
    def get_question_options(self, instance):
        question_type = instance.question_type
        if question_type.has_options:
            return instance.questionoption_set.extra(
                select={
                    'name': 'option'
                }
            ).values('id', 'name')
        elif question_type.has_default_choices:
            return question_type.questiontypechoice_set.extra(
                select={
                    'name': 'choice'
                }
            ).values('id', 'name')
        return None


class QuestionDetailSerializer(ListQuestionSerializer):
    pass


class ImportQuestionSerializer(CSVFileInputSerializer):
    pass
