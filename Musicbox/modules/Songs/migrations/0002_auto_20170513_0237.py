# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-13 02:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Songs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_comment', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='comments',
            name='song',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.AlterField(
            model_name='song',
            name='category',
            field=models.CharField(choices=[('ClA', 'Classical'), ('LAT', 'Latin'), ('ROC', 'Rock'), ('MET', 'Metal'), ('FOL', 'Folklore'), ('COU', 'Country'), ('ELE', 'Electronic'), ('POP', 'Pop'), ('ALT', 'Alternative'), ('RNB', 'R&B-Soul')], max_length=100),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song_comments', to='Songs.Song'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
