# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-23 12:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0008_main_table_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='text',
            new_name='description',
        ),
    ]