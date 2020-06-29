from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.capital.models import Capital, MoneyRecord
from apps.capital.serializers import CapitalModelsSerializer, MoneyRecordTasksModelsSerializer
from apps.utils.utils import Pagination
from apps.capital.filters import CapitalFilter, MoneyRecordTasksFilter


class CapitalViewSet(viewsets.ModelViewSet):
    """
    create: 资金明细 - 新增资金明细
    list: 资金明细 - 查询多笔资金明细
    retrieve: 资金明细 - 查询单条资金明细
    update: 资金明细 - 更新资金明细（覆盖更新模式）
    partial_update: 资金明细 - 更新资金明细（部分更新模式）
    delete: 资金明细 - 删除资金明细
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Capital.objects.all().order_by('-add_time')
    serializer_class = CapitalModelsSerializer
    lookup_field = 'capital_id'
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = CapitalFilter


class MoneyRecordViewSet(viewsets.ModelViewSet):
    """
    create: 提现记录 - 新增提现记录
    list: 提现记录 - 查询多条提现记录
    retrieve: 提现记录 - 查询单条提现记录
    update: 提现记录 - 更新提现记录（覆盖更新模式）
    partial_update: 提现记录 - 更新提现记录（部分更新模式）
    delete: 提现记录 - 删除提现记录
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = MoneyRecord.objects.all().order_by('-add_time')
    serializer_class = MoneyRecordTasksModelsSerializer

    lookup_field = 'record_id'
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = MoneyRecordTasksFilter


