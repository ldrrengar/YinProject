from rest_framework import serializers

from apps.tasks.models import Tasks, CompleteTasks, Banner, TasksType


class TasksTypeModelsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        depth = 1
        model = TasksType
        fields = '__all__'


class TasksModelsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        c_models = super(TasksModelsSerializer, self).create(validated_data=validated_data)
        # 默认为当前用户为创建人
        c_models.created = self.context['request'].user
        c_models.save()
        return c_models

    class Meta:
        depth = 1
        model = Tasks
        fields = ['tasks_id', 'url', 'target_times', 'completed_times', 'tasks_name', 'cost', 'total_cost', 'state',
                  'type', 'created', 'add_time']


class CompleteTasksModelsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        depth = 1
        model = CompleteTasks
        fields = ['execute_id', 'tasks_id', 'complete_user', 'price', 'image', 'state', 'remarks', 'add_time']


class BannerModelsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        depth = 1
        model = Banner
        fields = '__all__'


class CompleteTasksCreateModelsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    tasks_id = serializers.PrimaryKeyRelatedField(queryset=Tasks.objects.all())

    def create(self, validated_data):
        c_models = super(CompleteTasksCreateModelsSerializer, self).create(validated_data=validated_data)
        # 默认为当前用户为创建人
        c_models.complete_user = self.context['request'].user
        c_models.save()
        return c_models

    class Meta:
        depth = 1
        model = CompleteTasks
        fields = ['execute_id', 'tasks_id', 'complete_user', 'price', 'image', 'state', 'remarks', 'add_time']