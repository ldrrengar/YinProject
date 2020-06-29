# Generated by Django 2.1.1 on 2020-06-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20200626_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completetasks',
            name='state',
            field=models.CharField(choices=[('0', '待审核'), ('1', '已驳回'), ('2', '已完成')], default='1', help_text='状态 0：已完成,1：待审核,2:已驳回', max_length=10, verbose_name='状态'),
        ),
    ]
