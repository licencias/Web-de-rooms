# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestionjuegos', '0003_auto_20171018_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='consola',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Gestionjuegos.consola'),
            preserve_default=False,
        ),
    ]
