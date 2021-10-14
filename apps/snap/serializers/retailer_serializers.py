from rest_framework import serializers

from apps.snap.models import SnapRetailer


class SnapRetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapRetailer
        fields = '__all__'


class AddSnapRetailerSerializer(SnapRetailerSerializer):
    name = serializers.ListSerializer(child=serializers.CharField())

    class Meta(SnapRetailerSerializer.Meta):
        fields = (
            'name',
        )


class ListSnapRetailerSerializer(SnapRetailerSerializer):
    class Meta(SnapRetailerSerializer.Meta):
        fields = (
            'id',
            'name',
        )


class BasicListSnapRetailerSerializer(SnapRetailerSerializer):

    class Meta(SnapRetailerSerializer.Meta):
        fields = (
            'id',
            'name'
        )


class UpdateSnapRetailerSerializer(SnapRetailerSerializer):
    class Meta(SnapRetailerSerializer.Meta):
        fields = (
            'name',
        )

