# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admintool', '0006_auto_20150119_0728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expensetarget',
            old_name='user_id',
            new_name='user',
        ),
    ]
