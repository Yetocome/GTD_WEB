# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-14 08:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtd', '0005_auto_20161214_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='current_pomodores',
        ),
    ]
