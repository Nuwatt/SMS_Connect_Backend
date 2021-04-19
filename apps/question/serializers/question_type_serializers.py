from rest_framework import serializers

from apps.question.models import QuestionType


class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = '__all__'


class AddQuestionTypeSerializer(QuestionTypeSerializer):
    class Meta(QuestionTypeSerializer.Meta):
        fields = (
            'name',
        )


class ListQuestionTypeSerializer(AddQuestionTypeSerializer):
    class Meta(AddQuestionTypeSerializer.Meta):
        fields = AddQuestionTypeSerializer.Meta.fields + (
            'id',
        )


class QuestionDetailSerializer(ListQuestionTypeSerializer):
    pass
