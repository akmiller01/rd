# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.TextField(),
        ),
    ]
