# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0004_tasting_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasting',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 11, 15, 20, 24, 7, 773704, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
    ]
