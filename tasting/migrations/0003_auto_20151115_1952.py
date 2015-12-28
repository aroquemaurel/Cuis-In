# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0002_auto_20151115_1950'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Whiskies',
            new_name='Whisky',
        ),
    ]
