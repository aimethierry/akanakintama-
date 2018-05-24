# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image1',
            field=models.FileField(null=True, upload_to=b'media/', blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='image2',
            field=models.FileField(null=True, upload_to=b'media/', blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='image3',
            field=models.FileField(null=True, upload_to=b'media/', blank=True),
        ),
    ]
