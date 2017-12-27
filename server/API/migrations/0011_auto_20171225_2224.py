# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-25 22:24
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations
import server.API.models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0010_auto_20171224_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image_link',
            field=cloudinary.models.CloudinaryField(blank=True, default='default.png', max_length=255, null=True, validators=[server.API.models.ValidateFileType('jpg', 'jpeg', 'png', 'bmp', 'gif')], verbose_name='image'),
        ),
    ]
