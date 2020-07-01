from random import choice

from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from apps.users.models import UserProfile, Member, VerifyCode
from apps.users.serializers import UserProfileModelsSerializer, MemberModelsSerializer, VerifyCodeModelsSerializer, \
    UserRegSerializer, PasswordResetSerializer
from apps.utils.utils import Pagination
from apps.users.filters import UserProfileFilter, MemberTasksFilter
from apps.utils.common import send__sms

User = get_user_model()


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    create: 用户信息 - 新增用户信息
    list: 用户信息 - 查询多笔用户信息
    retrieve: 用户信息 - 查询单条用户信息
    update: 用户信息 - 更新用户信息（覆盖更新模式）
    partial_update: 用户信息 - 更新用户信息（部分更新模式）
    delete: 用户信息 - 删除用户信息
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = UserProfile.objects.all().order_by('-date_joined')
    serializer_class = UserProfileModelsSerializer
    lookup_field = 'username'
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = UserProfileFilter


class MemberViewSet(viewsets.ModelViewSet):
    """
    create: 会员信息 - 新增会员信息
    list: 会员信息 - 查询多笔会员信息
    retrieve: 会员信息 - 查询单条会员信息
    update: 会员信息 - 更新会员信息（覆盖更新模式）
    partial_update: 会员信息 - 更新会员信息（部分更新模式）
    delete: 会员信息 - 删除会员信息
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Member.objects.all().order_by('-add_time')
    serializer_class = MemberModelsSerializer

    lookup_field = 'member_id'
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = MemberTasksFilter


class SmsCodeViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """
    验证码发送
    """
    queryset = VerifyCode.objects.all()
    serializer_class = VerifyCodeModelsSerializer

    def generate_code(self):
        """
        生成六位数字的验证码
        """
        seeds = "1234567890"
        random_str = []
        for i in range(6):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # 验证合法
        serializer.is_valid(raise_exception=True)
        # 判断该手机号是否进行过注册
        mobile = serializer.validated_data["mobile"]

        # 生成验证码
        code = self.generate_code()

        code_record = VerifyCode(code=code, mobile=mobile)
        code_record.save()
        model = "SMS_194050695"
        params = {"code": code}
        sms_status = send__sms(mobile, model, params)
        # sms_status = {"Code": "OK"}
        print(code)
        if sms_status["Code"] != 'OK':
            return Response({
                "code": [sms_status["Message"]]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'mobile': mobile}, status=status.HTTP_201_CREATED)


class UserRegViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """用户注册"""
    serializer_class = UserRegSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        # re_dict["name"] = user.name if user.name else user.username
        re_dict["username"] = user.username
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class PasswordResetViewSet(UpdateModelMixin, viewsets.GenericViewSet):
    """用户密码修改"""
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = PasswordResetSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
