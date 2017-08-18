# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_auto_20170808_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.CharField(default='Generic description', max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='rule_version',
            field=models.CharField(choices=[('DSA4', 'Das Schwarze Auge, v4.1'), ('SPLITTERMOND', 'Splittermond'), ('GENERAL', 'Generic setting')], default='DEFAULT', max_length=20),
        ),
    ]
