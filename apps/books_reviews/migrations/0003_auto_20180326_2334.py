# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-26 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_reviews', '0002_auto_20180326_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
