# Generated by Django 2.1.1 on 2020-06-27 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_auto_20200627_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间'),
        ),
    ]
