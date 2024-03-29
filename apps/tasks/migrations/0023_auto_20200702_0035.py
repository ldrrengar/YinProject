# Generated by Django 2.1.1 on 2020-07-02 00:35

import apps.tasks.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0022_auto_20200702_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completetasks',
            name='image',
        ),
        migrations.AddField(
            model_name='completetasks',
            name='image1',
            field=models.ImageField(default=1, storage=apps.tasks.storage.ImageStorage(), upload_to='img/%Y%m%d', verbose_name='任务图片1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='completetasks',
            name='image2',
            field=models.ImageField(blank=True, null=True, storage=apps.tasks.storage.ImageStorage(), upload_to='img/%Y%m%d', verbose_name='任务图片2'),
        ),
        migrations.AddField(
            model_name='completetasks',
            name='image3',
            field=models.ImageField(blank=True, null=True, storage=apps.tasks.storage.ImageStorage(), upload_to='img/%Y%m%d', verbose_name='任务图片3'),
        ),
        migrations.AddField(
            model_name='completetasks',
            name='image4',
            field=models.ImageField(blank=True, null=True, storage=apps.tasks.storage.ImageStorage(), upload_to='img/%Y%m%d', verbose_name='任务图片4'),
        ),
        migrations.AddField(
            model_name='completetasks',
            name='image5',
            field=models.ImageField(blank=True, null=True, storage=apps.tasks.storage.ImageStorage(), upload_to='img/%Y%m%d', verbose_name='任务图片5'),
        ),
        migrations.AddField(
            model_name='completetasks',
            name='image6',
            field=models.ImageField(blank=True, null=True, storage=apps.tasks.storage.ImageStorage(), upload_to='img/%Y%m%d', verbose_name='任务图片6'),
        ),
        migrations.DeleteModel(
            name='ImageInfo',
        ),
    ]
