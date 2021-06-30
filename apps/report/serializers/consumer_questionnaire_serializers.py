from rest_framework import serializers


class YesNoQuestionReportSerializer(serializers.Serializer):
    question_statement = serializers.CharField()
    yes = serializers.FloatField()
    no = serializers.FloatField()


class NumericQuestionReportSerializer(serializers.Serializer):
    question_statement = serializers.CharField()
    value = serializers.DecimalField(default=0, decimal_places=2, max_digits=10)


class RatingOneToThreeReportSerializer(serializers.Serializer):
    question_statement = serializers.CharField()
    rating_one = serializers.FloatField()
    rating_two = serializers.FloatField()
    rating_three = serializers.FloatField()


class RatingOneToFiveReportSerializer(RatingOneToThreeReportSerializer):
    rating_four = serializers.FloatField()
    rating_five = serializers.FloatField()


class RatingOneToTenReportSerializer(RatingOneToFiveReportSerializer):
    rating_six = serializers.FloatField()
    rating_seven = serializers.FloatField()
    rating_eight = serializers.FloatField()
    rating_nine = serializers.FloatField()
    rating_ten = serializers.FloatField()
