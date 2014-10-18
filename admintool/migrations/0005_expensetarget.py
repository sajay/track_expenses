# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admintool', '0004_auto_20141004_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseTarget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan_type', models.CharField(max_length=25)),
                ('yr_m', models.CharField(max_length=10)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('user', models.CharField(max_length=25)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('expenseCategory', models.ForeignKey(to='admintool.ExpenseCategory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
