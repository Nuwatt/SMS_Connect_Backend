from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_serializer_method

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.question.models import QuestionTypeChoice, QuestionOption
from apps.response.models import Response, Answer


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'


class StartQuestionnaireSerializer(ResponseSerializer):
    class Meta(ResponseSerializer.Meta):
        fields = (
            'store',
            'latitude',
            'longitude'
        )
        extra_kwargs = {
            'store': {
                'required': True
            }
        }


class SummitQuestionnaireResponseSerializer(serializers.ModelSerializer):
    text_answer = serializers.CharField(required=False)
    numeric_answer = serializers.FloatField(required=False)
    image_answer = serializers.ListSerializer(
        child=serializers.CharField(),
        required=False
    )
    choice_answer = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=QuestionTypeChoice.objects.unarchived()
    )
    option_answer = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=QuestionOption.objects.unarchived(),
        many=True
    )

    class Meta:
        model = Answer
        fields = (
            'question',
            'text_answer',
            'numeric_answer',
            'choice_answer',
            'text_answer',
            'option_answer',
            'image_answer'
        )

    def validate(self, attrs):
        # 1. check for field required
        question_type = attrs.get('question').question_type
        if question_type.has_options or question_type.has_default_choices:
            if question_type.has_options:
                if not attrs.get('option_answer', None):
                    raise ValidationError({
                        'option_answer': _('Option Answer is required for this question.')
                    })
                self.validate_option(attrs.get('question'), attrs.get('option_answer'))
            elif question_type.has_default_choices:
                if not attrs.get('choice_answer', None):
                    raise ValidationError({
                        'choice_answer': _('Choice Answer is required for this question.')
                    })
                self.validate_choice(question_type, attrs.get('choice_answer'))
        else:
            if question_type.name == 'Pictures' and not attrs.get('image_answer', None):
                raise ValidationError({
                    'image_answer': _('Image Answer is required for this question.')
                })
            elif question_type.name.lower() == 'text' and not attrs.get('text_answer', None):
                raise ValidationError({
                    'text_answer': _('Text Answer is required for this question.')
                })
            elif question_type.name.lower() == 'numeric' and not attrs.get('numeric_answer', None):
                raise ValidationError({
                    'numeric_answer': _('Numeric Answer is required for this question.')
                })
        return attrs

    def validate_option(self, question, option):
        if not all(question == item.question for item in option):
            raise ValidationError({
                'option_answer': _('Options don\'t belong to same question.')
            })

    def validate_choice(self, question_type, choice):
        if question_type != choice.question_type:
            raise ValidationError({
                'choice_answer': _('Choice don\'t belong to same question type.')
            })

    def validate_question(self, value):
        questionnaire = self.context['view'].get_object().questionnaire
        if value.questionnaire != questionnaire:
            raise ValidationError(_('Question is not of same questionnaire.'))
        return value


class BulkSummitQuestionnaireResponseSerializer(serializers.Serializer):
    data = SummitQuestionnaireResponseSerializer(many=True, required=True)

    def validate(self, attrs):
        # 1. check duplicate of question
        unique_question = []
        for item in attrs.get('data'):
            if item.get('question') in unique_question:
                raise ValidationError({
                    'data': _('Data has duplicate questions.')
                })
            unique_question.append(item.get('question'))
        return attrs


class ListAgentResponseHistorySerializer(serializers.Serializer):
    id = serializers.CharField()
    questionnaire = serializers.CharField()
    questionnaire_type = serializers.CharField(source='questionnaire.questionnaire_type')
    start_date_time = serializers.DateTimeField(source='created', format='%d-%m-%Y - %H:%M %p')
    completed_at = serializers.DateTimeField(format='%d-%m-%Y - %H:%M %p')


data = [
    {
        "question": "Q0001",
        "text_answer": "20"
    },
    {
        "question": "Q0002",
        "image_answer": "image file"
    },
    {
        "question": "Q0003",
        "choice_answer": "1"
    },
    {
        "question": "Q0004",
        "option_answer": ["1", "2"]
    },
]


class ListAgentResponseSerializer(serializers.Serializer):
    questionnaire_id = serializers.CharField(source='questionnaire.id')
    questionnaire_name = serializers.CharField(source='questionnaire.name')
    questionnaire_type = serializers.CharField(source='questionnaire.questionnaire_type')
    start_time = serializers.DateTimeField(source='created', format='%p %H:%M')
    finish_time = serializers.DateTimeField(source='completed_at', format='%p %H:%M')
    completed_date = serializers.DateTimeField(source='completed_at', format='%d/%m/%Y')
    completed_duration = serializers.CharField()
    country = serializers.CharField(source='store.city.country')
    city = serializers.CharField(source='store.city')
    retailer = serializers.CharField(source='store.retailer')
    store = serializers.CharField()
    channel = serializers.CharField(source='store.retailer.channel')
    gps = serializers.CharField(source='coordinates')


class ListQuestionnaireResponseSerializer(serializers.Serializer):
    user_id = serializers.CharField(source='agent.id')
    username = serializers.CharField(source='agent.user.username')
    completed_date = serializers.DateTimeField(source='completed_at', format='%d/%m/%Y')
    number_of_answers = serializers.IntegerField()
    start_time = serializers.DateTimeField(source='created', format='%p %H:%M')
    finish_time = serializers.DateTimeField(source='completed_at', format='%p %H:%M')
    country = serializers.CharField(source='store.city.country')
    city = serializers.CharField(source='store.city')
    retailer = serializers.CharField(source='store.retailer')
    store = serializers.CharField()
    channel = serializers.CharField(source='store.retailer.channel')


class ListQuestionnaireAnswerSerializer(serializers.Serializer):
    question_id = serializers.CharField()
    # question_type = serializers.CharField(source='question.question_type.name')
    question_type = serializers.CharField()
    # question = serializers.CharField(source='question.statement')
    question = serializers.CharField()
    # answer = serializers.SerializerMethodField()
    answer = serializers.ListSerializer(child=serializers.CharField())

    # @swagger_serializer_method(serializer_or_field=serializers.ListSerializer(child=serializers.CharField()))
    # def get_answer(self, instance):
    #     question_type = instance.question.question_type
    #     if question_type.name == 'Numeric':
    #         return [instance.numericanswer.numeric]
    #     elif question_type.name == 'Text':
    #         return [instance.textanswer.text]
    #     elif question_type.name == 'Image':
    #         return [item.image.url for item in instance.imageanswer_set.all()]
    #     elif question_type.has_default_choices:
    #         return instance.choiceanswer_set.values_list('choice__choice', flat=True)
    #     elif question_type.has_options:
    #         return instance.optionanswer_set.values_list('option__option', flat=True)
    #     return None
