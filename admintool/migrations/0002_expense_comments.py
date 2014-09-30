# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admintool', '0001_squashed_0006_auto_20140924_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='comments',
            field=models.CharField(default='test comments', max_length=100),
            preserve_default=False,
        ),
    ]
