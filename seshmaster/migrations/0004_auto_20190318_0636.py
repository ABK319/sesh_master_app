# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-18 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seshmaster', '0003_auto_20190318_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nightclub',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
