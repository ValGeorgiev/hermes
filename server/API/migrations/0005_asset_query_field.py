# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_auto_20171122_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='query_field',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
    ]
