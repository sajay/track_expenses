# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('admintool', '0002_auto_20140921_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=25)),
                ('category_desc', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=25)),
                ('type_desc', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='expense',
            name='expenseCategory',
            field=models.ForeignKey(default=1, to='admintool.ExpenseCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='expenseType',
            field=models.ForeignKey(default=1, to='admintool.ExpenseType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='expense_date',
            field=models.DateField(default=datetime.date(2014, 9, 22)),
            preserve_default=False,
        ),
    ]
