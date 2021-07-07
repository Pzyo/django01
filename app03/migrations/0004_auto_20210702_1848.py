# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-07-02 10:48
from __future__ import unicode_literals

import app03.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0003_auto_20210701_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='kucun',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='maichu',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='myfield',
            field=app03.models.MyCharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='app03.Author'),
        ),
    ]