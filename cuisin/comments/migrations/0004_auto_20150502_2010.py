# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_comment_infoauthor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='infoAuthor',
            field=models.ForeignKey(to='members.UserInfo', on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
