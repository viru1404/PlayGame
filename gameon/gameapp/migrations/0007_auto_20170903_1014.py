# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 10:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0006_activeusers_qid2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activeusers',
            name='answer',
        ),
        migrations.AddField(
            model_name='activeusers',
            name='answer1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='activeusers',
            name='answer2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='activeusers',
            name='answer3',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='activeusers',
            name='answer4',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='activeusers',
            name='answer5',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='activeusers',
            name='qid3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qid3', to='gameapp.Questions'),
        ),
        migrations.AddField(
            model_name='activeusers',
            name='qid4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qid4', to='gameapp.Questions'),
        ),
        migrations.AddField(
            model_name='activeusers',
            name='qid5',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qid5', to='gameapp.Questions'),
        ),
        migrations.AlterField(
            model_name='activeusers',
            name='qid1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qid1', to='gameapp.Questions'),
        ),
        migrations.AlterField(
            model_name='activeusers',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
