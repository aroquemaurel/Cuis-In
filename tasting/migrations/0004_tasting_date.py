# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0003_auto_20151115_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasting',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 15, 20, 12, 10, 806852, tzinfo=utc), verbose_name=b"Date d'ajout", auto_now_add=True),
            preserve_default=False,
        ),
    ]
