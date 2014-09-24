# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('admintool', '0005_auto_20140923_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='date',
            new_name='created_on',
        ),
        migrations.AddField(
            model_name='expense',
            name='updated_on',
            field=models.DateTimeField(default=datetime.date(2014, 9, 24), auto_now_add=True),
            preserve_default=False,
        ),
    ]
