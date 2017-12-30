# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-29 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0019_auto_20171229_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='body_en',
            field=models.TextField(blank=True, null=True, verbose_name='Body (English)'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='title_en',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='Title (English)'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='name_en',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='Name (English)'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='Name (English)'),
        ),
        migrations.AlterField(
            model_name='item',
            name='content_en',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Content (English)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Description (English)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_en',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Name (English)'),
        ),
        migrations.AlterField(
            model_name='site',
            name='config_name_en',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='Config name (English)'),
        ),
    ]
