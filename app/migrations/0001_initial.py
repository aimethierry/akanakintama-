# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('description', models.CharField(max_length=140, null=True, blank=True)),
                ('text', models.TextField()),
                ('image', models.FileField(null=True, upload_to=b'media/', blank=True)),
            ],
        ),
    ]
