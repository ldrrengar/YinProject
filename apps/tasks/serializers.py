from datetime import datetime

from django.contrib.auth import get_user_model
from django.db.models import Q, F
from rest_framework import serializers

from apps.tasks.models import Tasks, CompleteTasks, Banner, ImageInfo, Transfer

# from users.models import UserProfile
# from users.models import UserProfile

User = get_user_model()


# class TasksTypeModelsSerializer(serializers.ModelSerializer):
#     add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
#
#     class Meta:
#         depth = 1
#         model = TasksType
#         fields = '__all__'


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
        fields = ['tasks_id', 'url', 'target_times', 'completed_times', 'tasks_name', 'cost', 'complete_cost',
                  'total_cost', 'state', 'type', 'created', 'add_time']


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

    # tasks_id = serializers.PrimaryKeyRelatedField(queryset=Tasks.objects.all())
    # image = serializers.PrimaryKeyRelatedField(queryset=ImageInfo.objects.all())

    def create(self, validated_data):
        sign = CompleteTasks.objects.filter(tasks_id=validated_data['tasks_id'], state__in=["0", "2"],
                                            complete_user=self.context["request"].user).count()
        if sign >0:
            raise serializers.ValidationError('提交失败：已提交过该任务，无法再次提交')
        # ①-获取任务分类
        task_type = validated_data['tasks_id'].type
        # a = Tasks.objects.filter(tasks_id=tasks_id)
        # task_type = Tasks.objects.filter(tasks_id=tasks_id).values("type")[0]["type"]
        # ②-获取用户的普通任务次数和会员任务次数
        if task_type == "0":
            # 获取今天已完成的普通任务和可以完成的普通任务
            today = datetime.now()
            year = today.strftime("%Y")
            month = today.strftime("%m")
            day = today.strftime("%d")
            # 今天已完成的普通任务个数
            num = CompleteTasks.objects.filter(
                Q(add_time__year=year) & Q(add_time__month=month) & Q(add_time__day=day) & Q(
                    tasks_id__type="0") & Q(complete_user=self.context["request"].user)).count()
            # 可以完成的普通任务个数
            sum_num = self.context["request"].user.member_level.common_num
            if num >= int(sum_num):
                raise serializers.ValidationError('提交失败：今日完成普通任务已达最大次数')

        elif task_type == "1":
            # 获取今天已完成的会员任务和可以完会员任务
            today = datetime.now()
            year = today.strftime("%Y")
            month = today.strftime("%m")
            day = today.strftime("%d")
            # 今天已完成的会员任务个数
            num = CompleteTasks.objects.filter(
                Q(add_time__year=year) & Q(add_time__month=month) & Q(add_time__day=day) & Q(
                    tasks_id__type="1") & Q(complete_user=self.context["request"].user)).count()
            # 可以完成的会员任务个数
            sum_num = self.context["request"].user.member_level.member_num
            if num >= int(sum_num):
                raise serializers.ValidationError('提交失败：今日完成会员任务已达最大次数')
        else:
            raise serializers.ValidationError('提交失败')
            # 创建完成任务的时候，任务完成条数增加1
        # tasks = Tasks.objects.filter(tasks_id=validated_data['tasks_id'].tasks_id).values('completed_times', 'target_times')[0]
        completed_times, target_times = validated_data['tasks_id'].completed_times, validated_data['tasks_id'].target_times
        if completed_times >= target_times:
            raise serializers.ValidationError('提交失败：该任务已完成')
        completed_times = completed_times + 1
        Tasks.objects.filter(tasks_id=validated_data['tasks_id'].tasks_id).update(completed_times=completed_times)
        c_models = super(CompleteTasksCreateModelsSerializer, self).create(validated_data=validated_data)
        # 默认为当前用户为创建人
        c_models.complete_user = self.context['request'].user
        c_models.save()
        return c_models

    class Meta:
        model = CompleteTasks
        fields = ['execute_id', 'tasks_id', 'complete_user', 'price', 'image', 'state', 'remarks', 'add_time']


class ImageInfoModelsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = ImageInfo
        fields = '__all__'


class HomePageModelsSerializer(serializers.ModelSerializer):
    ThreeData = serializers.SerializerMethodField()

    def get_ThreeData(self, obj):
        """
        获取首页三条数据
        tasks：今日任务数
        users：今日用户数
        completes：今日完成数
        :param obj:
        :return:
        """
        tasks = Tasks.objects.filter(target_times__gt=F('completed_times')).count()
        users = User.objects.all().count()
        today = datetime.now()
        # 今年
        year = today.strftime("%Y")
        month = today.strftime("%m")
        day = today.strftime("%d")
        completes = CompleteTasks.objects.filter(add_time__year=year).filter(add_time__month=month).filter(
            add_time__day=day).count()
        completes = CompleteTasks.objects.filter(
            Q(add_time__year=year) & Q(add_time__month=month) & Q(add_time__day=day)).count()
        # completes = CompleteTasks.objects.all().count()
        # completes = 1
        three_data = {
            "tasks": tasks,
            "users": users,
            "completes": completes
        }
        return three_data

    class Meta:
        model = Tasks
        fields = ('ThreeData',)


class MyTasksModelsSerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField()

    def get_state(self, obj):
        for i in obj.STATE_CHOICES:
            if i[0] == obj.state:
                return i[1]

    class Meta:
        model = Tasks
        fields = ('tasks_id', 'tasks_name', 'target_times', 'completed_times', 'state', 'total_cost')


class TransferModelsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Transfer
        fields = '__all__'
