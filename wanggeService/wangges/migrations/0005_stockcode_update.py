# Generated by Django 2.0.2 on 2018-04-06 14:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wangges', '0004_auto_20180406_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockcode',
            name='update',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='上市日期'),
            preserve_default=False,
        ),
    ]
