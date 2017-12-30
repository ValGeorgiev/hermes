# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_remove_asset_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='client_id',
            field=models.CharField(default=uuid.uuid4, max_length=128),
        ),
    ]
