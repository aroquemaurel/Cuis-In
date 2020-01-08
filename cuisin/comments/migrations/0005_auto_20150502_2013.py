# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20150502_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='infoAuthor',
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(to='members.UserInfo', on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
