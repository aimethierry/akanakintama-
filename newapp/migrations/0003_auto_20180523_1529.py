# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='ost',
            new_name='post',
        ),
    ]
