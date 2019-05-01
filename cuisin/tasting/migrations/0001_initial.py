# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoffeeCountry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tasting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('flair', models.TextField()),
                ('mouth', models.TextField()),
                ('color', models.TextField()),
                ('note', models.IntegerField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('tasting_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tasting.Tasting')),
                ('altitude', models.IntegerField()),
                ('strength', models.IntegerField(max_length=2)),
                ('country', models.ForeignKey(to='tasting.CoffeeCountry')),
            ],
            options={
            },
            bases=('tasting.tasting',),
        ),
        migrations.CreateModel(
            name='Whiskies',
            fields=[
                ('tasting_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tasting.Tasting')),
                ('old', models.IntegerField()),
            ],
            options={
            },
            bases=('tasting.tasting',),
        ),
        migrations.CreateModel(
            name='WhiskyType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('tasting_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tasting.Tasting')),
                ('year', models.IntegerField()),
            ],
            options={
            },
            bases=('tasting.tasting',),
        ),
        migrations.AddField(
            model_name='whiskies',
            name='type',
            field=models.ForeignKey(to='tasting.WhiskyType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tasting',
            name='category',
            field=models.ForeignKey(to='tasting.Category'),
            preserve_default=True,
        ),
    ]
