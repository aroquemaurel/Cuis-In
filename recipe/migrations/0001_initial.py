# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('note', models.IntegerField(max_length=2)),
                ('hard', models.IntegerField(max_length=2)),
                ('serves', models.IntegerField(max_length=2)),
                ('preparationTime', models.IntegerField(max_length=4)),
                ('cuissonTime', models.IntegerField(max_length=4)),
                ('preparation', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b"Date d'ajout")),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
