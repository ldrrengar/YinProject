from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class Member(models.Model):
    """
    会员信息
    """
    CHOICES = (
        ("0", "无会员"),
        ("1", "青铜"),
        ("2", "白银"),
        ("3", "黄金"),
        ("4", "白金"),
        ("5", "钻石"),
    )
    member_id = models.AutoField(verbose_name="会员编号", primary_key=True, help_text="会员编号")
    member_name = models.CharField(verbose_name="会员等级名称", choices=CHOICES, max_length=10, help_text="会员等级名称")
    common_num = models.CharField(verbose_name="普通任务条数", max_length=10, help_text="普通任务条数")
    member_num = models.CharField(verbose_name="会员任务条数", max_length=10, help_text="会员任务条数")
    time = models.CharField(verbose_name="有效期限", max_length=11, help_text="有效期限：单位：年")
    place = models.CharField(verbose_name="价格", max_length=11, help_text="价格")
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now, help_text="添加时间")

    class Meta:
        verbose_name = "会员信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.member_id)


class UserProfile(AbstractUser):
    """
    用户信息
    """
    # GENDER_CHOICES = (
    #     ("male", u"男"),
    #     ("female", u"女")
    # )
    # 用户用手机注册，所以姓名，生日和邮箱可以为空
    name = models.CharField(verbose_name="昵称", max_length=30, null=True, blank=True, help_text="昵称")
    pay_password = models.CharField(verbose_name="支付密码", max_length=30, null=True, blank=True, help_text="支付密码")
    ZFB_name = models.CharField(verbose_name="支付宝名称", max_length=30, null=True, blank=True, help_text="支付宝名称")
    ZFB_account = models.CharField(verbose_name="支付宝账号",  max_length=30, null=True, blank=True, help_text="支付宝账号")
    task_num = models.CharField(verbose_name="普通任务条数", max_length=10, null=True, blank=True, help_text="普通任务条数")
    member_limit = models.CharField(verbose_name="会员到期日", max_length=10, null=True, blank=True,
                                    help_text="会员到期日 格式：2020-06-30")
    invitation_code = models.CharField(verbose_name="邀请码",  max_length=30, null=True, blank=True, help_text="邀请码")
    invitation_name = models.ForeignKey('self', verbose_name="邀请人",  max_length=30, null=True, blank=True,
                                        help_text="邀请人", to_field="username", on_delete=models.DO_NOTHING)
    member_level = models.ForeignKey(Member, null=True, blank=True, verbose_name="会员等级", help_text="会员等级",
                                     on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    验证码
    """
    code = models.CharField(verbose_name="验证码", max_length=10)
    mobile = models.CharField(verbose_name="电话", max_length=11)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "短信验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
