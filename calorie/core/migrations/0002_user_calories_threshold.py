# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-01-07 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='calories_threshold',
            field=models.IntegerField(default=2100),
        ),
    ]
