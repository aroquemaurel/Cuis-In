# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0007_auto_20151228_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whisky',
            name='degAlcool',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wine',
            name='degAlcool',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
