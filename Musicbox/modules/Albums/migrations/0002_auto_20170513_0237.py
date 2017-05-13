# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-13 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='category',
            field=models.CharField(choices=[('ClA', 'Classical'), ('LAT', 'Latin'), ('ROC', 'Rock'), ('MET', 'Metal'), ('FOL', 'Folklore'), ('COU', 'Country'), ('ELE', 'Electronic'), ('POP', 'Pop'), ('ALT', 'Alternative'), ('RNB', 'R&B-Soul')], max_length=100),
        ),
    ]
