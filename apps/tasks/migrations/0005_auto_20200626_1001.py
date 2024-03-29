# Generated by Django 2.1.1 on 2020-06-26 10:01

import apps.tasks.storage
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='completetasks',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, storage=apps.tasks.storage.ImageStorage(), upload_to='img/%Y/%m/%d', verbose_name='任务图片'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(storage=apps.tasks.storage.ImageStorage(), upload_to='img/%Y/%m/%d', verbose_name='轮播图片'),
        ),
    ]
