# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('matricula', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
