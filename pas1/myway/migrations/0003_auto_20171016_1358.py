# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myway', '0002_auto_20171012_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('matricula', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Aluno',
        ),
    ]
