# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-13 00:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Artists', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('category', models.CharField(choices=[('MET', 'Metal'), ('COU', 'Country'), ('ROC', 'Rock'), ('FOL', 'Folklore'), ('ALT', 'Alternative'), ('RNB', 'R&B-Soul'), ('ELE', 'Electronic'), ('POP', 'Pop'), ('LAT', 'Latin'), ('ClA', 'Classical')], max_length=100)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist_album', to='Artists.Artist')),
                ('user_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
