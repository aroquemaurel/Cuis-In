# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasting', '0006_tastingcategory_singulartitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='whisky',
            name='degAlcool',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wine',
            name='degAlcool',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
