# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-07-01 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0002_auto_20210701_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='app03.Author'),
        ),
    ]