# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-07-06 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0005_auto_20210706_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='app03.Author'),
        ),
    ]
