# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-13 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtd', '0003_auto_20161212_1700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scheduleitem',
            old_name='loop_time',
            new_name='loop_times',
        ),
        migrations.RenameField(
            model_name='scheduleitem',
            old_name='time',
            new_name='start_time',
        ),
        migrations.AddField(
            model_name='scheduleitem',
            name='loop_types',
            field=models.CharField(choices=[('Nope', '不循环'), ('Daily', '每天'), ('Weekly', '每周'), ('Monthly', '每月'), ('Yearly', '每年')], default='Nope', max_length=1),
        ),
    ]
