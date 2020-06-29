from datetime import datetime
from django.db import models

# Create your models here.


class News(models.Model):
    """
    新闻公告
    """
    new_id = models.AutoField(verbose_name="公告id", primary_key=True, help_text="公告id")
    new_title = models.CharField(verbose_name="公告标题", max_length=360, help_text="公告标题")
    new_content = models.CharField(verbose_name="公告内容", max_length=6400, help_text="公告内容")
    add_time = models.DateTimeField(verbose_name="创建时间", default=datetime.now, help_text="创建时间")

    class Meta:
        verbose_name = "新闻公告"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.new_id)

