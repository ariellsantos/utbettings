# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apuestas', '0005_auto_20171019_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='torneo',
            name='rol',
            field=models.BooleanField(default=False),
        ),
    ]