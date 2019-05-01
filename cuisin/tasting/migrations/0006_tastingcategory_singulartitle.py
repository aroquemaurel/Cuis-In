# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0005_tasting_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='tastingcategory',
            name='singularTitle',
            field=models.CharField(default='Whisky', max_length=128),
            preserve_default=False,
        ),
    ]
