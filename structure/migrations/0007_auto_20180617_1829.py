# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-17 15:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0006_auto_20180616_1517'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Table',
            new_name='main',
        ),
    ]