from rest_framework import serializers

from apps.core.serializers import (
    CSVFileInputSerializer,
    IdNameSerializer,
    IdNameCharSerializer
)
from apps.report.serializers.consumer_questionnaire_serializers import (
    YesNoQuestionReportSerializer,
    NumericQuestionReportSerializer
)
from apps.snap.models import ConsumerSnap


class ImportConsumerSnapSerializer(CSVFileInputSerializer):
    pass


class ConsumerSnapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumerSnap
        fields = '__all__'


class ListConsumerSnapSerializer(ConsumerSnapSerializer):
    country = serializers.CharField(source='city__country__name')
    city = serializers.CharField(source='city__name')
    category = serializers.CharField(source='sku__category__name')
    brand = serializers.CharField(source='sku__brand__name')
    channel = serializers.CharField(source='channel__name')
    sku = serializers.CharField(source='sku__name')
    question_type = serializers.CharField(source='question_type__name')

    class Meta(ConsumerSnapSerializer.Meta):
        fields = (
            'id', 'date', 'country', 'city', 'channel', 'category', 'brand',
            'sku', 'count', 'question_statement', 'question_type', 'total_yes',
            'total_no', 'rating_one_on_three', 'rating_two_on_three', 'rating_three_on_three',
            'rating_one_on_five', 'rating_two_on_five', 'rating_three_on_five', 'rating_four_on_five',
            'rating_five_on_five', 'rating_one_on_ten', 'rating_two_on_ten', 'rating_three_on_ten',
            'rating_four_on_ten', 'rating_five_on_ten', 'rating_six_on_ten', 'rating_seven_on_ten',
            'rating_eight_on_ten', 'rating_nine_on_ten', 'rating_ten_on_ten', 'average_numeric'
        )


class UpdateConsumerSnapSerializer(ConsumerSnapSerializer):
    class Meta(ConsumerSnapSerializer.Meta):
        fields = (
            'count', 'question_statement', 'question_type', 'total_yes',
            'total_no', 'rating_one_on_three', 'rating_two_on_three', 'rating_three_on_three',
            'rating_one_on_five', 'rating_two_on_five', 'rating_three_on_five', 'rating_four_on_five',
            'rating_five_on_five', 'rating_one_on_ten', 'rating_two_on_ten', 'rating_three_on_ten',
            'rating_four_on_ten', 'rating_five_on_ten', 'rating_six_on_ten', 'rating_seven_on_ten',
            'rating_eight_on_ten', 'rating_nine_on_ten', 'rating_ten_on_ten', 'average_numeric'
        )


class YesNoQuestionConsumerSnapReportSerializer(YesNoQuestionReportSerializer):
    pass


class RatingOneToThreeConsumerSnapReportSerializer(serializers.Serializer):
    question_statement = serializers.CharField()
    rating_one = serializers.FloatField(source='rating_one_on_three')
    rating_two = serializers.FloatField(source='rating_two_on_three')
    rating_three = serializers.FloatField(source='rating_three_on_three')


class RatingOneToFiveConsumerSnapReportSerializer(serializers.Serializer):
    question_statement = serializers.CharField()
    rating_one = serializers.FloatField(source='rating_one_on_five')
    rating_two = serializers.FloatField(source='rating_two_on_five')
    rating_three = serializers.FloatField(source='rating_three_on_five')
    rating_four = serializers.FloatField(source='rating_four_on_five')
    rating_five = serializers.FloatField(source='rating_five_on_five')


class RatingOneToTenConsumerSnapReportSerializer(serializers.Serializer):
    question_statement = serializers.CharField()
    rating_one = serializers.FloatField(source='rating_one_on_ten')
    rating_two = serializers.FloatField(source='rating_two_on_ten')
    rating_three = serializers.FloatField(source='rating_three_on_ten')
    rating_four = serializers.FloatField(source='rating_four_on_ten')
    rating_five = serializers.FloatField(source='rating_five_on_ten')
    rating_six = serializers.FloatField(source='rating_six_on_ten')
    rating_seven = serializers.FloatField(source='rating_seven_on_ten')
    rating_eight = serializers.FloatField(source='rating_eight_on_ten')
    rating_nine = serializers.FloatField(source='rating_nine_on_ten')
    rating_ten = serializers.FloatField(source='rating_ten_on_ten')


class NumericAverageConsumerSnapReportSerializer(NumericQuestionReportSerializer):
    pass


class BulkDeleteConsumerSnapSerializer(serializers.Serializer):
    snap_ids = serializers.ListSerializer(child=serializers.IntegerField())
