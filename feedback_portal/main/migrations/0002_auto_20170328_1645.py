# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-28 16:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestfeedback',
            name='end_date',
            field=models.DateField(default=datetime.date(2017, 4, 7)),
        ),
        migrations.AlterField(
            model_name='requestfeedback',
            name='start_date',
            field=models.DateField(default=datetime.date(2017, 3, 28)),
        ),
    ]