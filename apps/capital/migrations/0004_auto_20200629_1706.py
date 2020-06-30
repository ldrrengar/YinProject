# Generated by Django 2.1.1 on 2020-06-29 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capital', '0003_auto_20200628_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneyrecord',
            name='state',
            field=models.CharField(choices=[('0', '待放款'), ('1', '已放款'), ('2', '已驳回')], default='1', help_text='状态  0：待放款,1:已放款,2:已驳回', max_length=10, verbose_name='状态'),
        ),
    ]