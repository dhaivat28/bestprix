# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-13 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0008_delete_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.CharField(max_length=100)),
                ('p_id', models.CharField(max_length=100)),
                ('seller', models.CharField(max_length=100)),
            ],
        ),
    ]