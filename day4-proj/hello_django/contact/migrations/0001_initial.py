# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-10-24 13:38
from __future__ import unicode_literals

from django.db import migrations, models

# 定义models的类模型后，使用 “python3 manage.py makemigration” 命令后生成的模型信息


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('phone_num', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=400)),
            ],
        ),
    ]
