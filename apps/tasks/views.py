from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.tasks.models import Tasks, CompleteTasks, Banner, TasksType
from apps.tasks.serializers import TasksModelsSerializer, CompleteTasksModelsSerializer, BannerModelsSerializer, \
    TasksTypeModelsSerializer, CompleteTasksCreateModelsSerializer
from apps.utils.utils import Pagination
from apps.tasks.filters import TasksFilter, CompleteTasksFilter, TasksTypeFilter


class TasksTypeViewSet(viewsets.ModelViewSet):
    """
    create: 任务类型 - 新增任务类型
    list: 任务类型 - 查询多笔任务类型
    retrieve: 任务类型 - 查询单条任务类型
    update: 任务类型 - 更新任务类型（覆盖更新模式）
    partial_update: 任务类型 - 更新任务类型（部分更新模式）
    delete: 任务类型 - 删除任务类型
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = TasksType.objects.all().order_by('-add_time')
    serializer_class = TasksTypeModelsSerializer
    lookup_field = 'type_id'
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = TasksTypeFilter


class TasksViewSet(viewsets.ModelViewSet):
    """
    create: 任务信息 - 新增任务信息
    list: 任务信息 - 查询多笔任务信息
    retrieve: 任务信息 - 查询单条任务信息
    update: 任务信息 - 更新任务信息（覆盖更新模式）
    partial_update: 任务信息 - 更新任务信息（部分更新模式）
    delete: 任务信息 - 删除任务信息
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Tasks.objects.all().order_by('-add_time')
    serializer_class = TasksModelsSerializer
    lookup_field = 'tasks_id'
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = TasksFilter


class CompleteTasksViewSet(viewsets.ModelViewSet):
    """
    create: 任务完成信息 - 新增任务完成信息
    list: 任务完成信息 - 查询多笔任务完成信息
    retrieve: 任务完成信息 - 查询单条任务完成信息
    update: 任务完成信息 - 更新任务完成信息（覆盖更新模式）
    partial_update: 任务完成信息 - 更新任务完成信息（部分更新模式）
    delete: 任务完成信息 - 删除任务完成信息
    """
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = CompleteTasks.objects.all().order_by('-add_time')
    serializer_class = CompleteTasksModelsSerializer

    lookup_field = 'execute_id'
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = CompleteTasksFilter

    # def get_queryset(self):
    #     return CompleteTasks.objects.filter(complete_user=self.request.user).order_by('-add_time')

    # 根据请求类型不同，设置不同的序列化器
    def get_serializer_class(self):
        if self.action in ("create"):
            return CompleteTasksCreateModelsSerializer
        else:
            return CompleteTasksModelsSerializer


class BannerViewSet(viewsets.ModelViewSet):
    """
    create: 首页轮播的图片 - 新增首页轮播的图片
    list: 首页轮播的图片 - 查询多笔首页轮播的图片
    retrieve: 首页轮播的图片 - 查询首页轮播的图片
    update: 首页轮播的图片 - 更新首页轮播的图片（覆盖更新模式）
    partial_update: 首页轮播的图片 - 更新首页轮播的图片（部分更新模式）
    delete: 首页轮播的图片 - 删除首页轮播的图片
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Banner.objects.all().order_by('-add_time')
    serializer_class = BannerModelsSerializer

    lookup_field = 'index'
