# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(default=b'', max_length=128)),
                ('note', models.IntegerField(max_length=2)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b"Date d'ajout")),
                ('reservation', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('phone', models.CharField(default=b'', max_length=16)),
                ('website', models.CharField(default=b'', max_length=128)),
                ('address', models.CharField(default=b'', max_length=128)),
                ('postalcode', models.CharField(default=b'', max_length=16)),
                ('city', models.CharField(default=b'', max_length=128)),
                ('tags', models.ManyToManyField(to='tags.Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
