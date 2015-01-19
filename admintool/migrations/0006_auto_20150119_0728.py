# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admintool', '0005_expensetarget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expensetarget',
            name='user',
        ),
        migrations.AddField(
            model_name='expensetarget',
            name='user_id',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
