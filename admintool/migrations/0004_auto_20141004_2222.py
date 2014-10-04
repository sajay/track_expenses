# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admintool', '0003_expense_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount_spent',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
    ]
