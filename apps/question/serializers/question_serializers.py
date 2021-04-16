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
    question_options = serializers.ListSerializer(
        child=serializers.CharField(),
        source='questionoption_set'
    )

    class Meta(AddQuestionSerializer.Meta):
        fields = AddQuestionSerializer.Meta.fields + (
            'id',
        )


class QuestionDetailSerializer(ListQuestionSerializer):
    pass
