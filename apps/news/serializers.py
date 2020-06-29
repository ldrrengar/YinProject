from rest_framework import serializers

from apps.news.models import News


class NewsModelsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = News
        fields = '__all__'



