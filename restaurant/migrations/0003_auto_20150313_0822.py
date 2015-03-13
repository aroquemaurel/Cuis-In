# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('restaurant', '0002_restaurant_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='city',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(default=b'', max_length=16),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='postalcode',
            field=models.CharField(default=b'', max_length=16),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='website',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
    ]
