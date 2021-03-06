# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-26 11:26
from __future__ import unicode_literals

from django.db import migrations


def populate_site_config_name(apps, schema_editor):
    Site = apps.get_model('API', 'Site')
    for ind, site in enumerate(Site.objects.all()):
        if not site.config_name:
            site.config_name = "generated_config_name_{}".format(ind)
            site.save()


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0012_auto_20171225_2228'),
    ]

    operations = [
        migrations.RunPython(populate_site_config_name),
    ]
