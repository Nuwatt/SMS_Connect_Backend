from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from apps.question.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AddQuestionSerializer(QuestionSerializer):
    question_options = serializers.ListSerializer(child=serializers.CharField())
    question_statement = serializers.CharField()

    class Meta(QuestionSerializer.Meta):
        fields = (
            'question_type',
            'question_statement',
            'question_options',
            'brand',
            'sku',
        )


class ListQuestionSerializer(AddQuestionSerializer):
    question_options = serializers.SerializerMethodField()

    class Meta(AddQuestionSerializer.Meta):
        fields = AddQuestionSerializer.Meta.fields + (
            'id',
        )

    @swagger_serializer_method(serializer_or_field=serializers.ListSerializer(child=serializers.CharField()))
    def get_question_options(self, instance):
        return instance.questionoption_set.values_list('option', flat=True)


class QuestionDetailSerializer(ListQuestionSerializer):
    pass
