from rest_framework import serializers

from apps.capital.models import Capital, MoneyRecord


class CapitalModelsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Capital
        fields = '__all__'


class MoneyRecordTasksModelsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        depth = 1
        model = MoneyRecord
        fields = '__all__'


