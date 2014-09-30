# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from admintool.models import ExpenseCategory, VendorType, ExpenseType


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# admintool.migrations.0005_auto_20140923_1900


def load_data(apps, schema_editor):
    ExpenseCategory(category_name="Groceries",).save()
    ExpenseCategory(category_name="Books",).save()
    ExpenseCategory(category_name="School Supplies",).save()
    ExpenseCategory(category_name="Utilities",).save()
    ExpenseCategory(category_name="Insurance",).save()
    ExpenseCategory(category_name="Medical",).save()
    ExpenseCategory(category_name="Gas",).save()
    ExpenseCategory(category_name="Mortgage",).save()
    ExpenseCategory(category_name="Travel",).save()
    ExpenseCategory(category_name="Restaurant",).save()
    ExpenseCategory(category_name="Taxes",).save()

    ExpenseType(type_name="Cash",).save()
    ExpenseType(type_name="Check",).save()
    ExpenseType(type_name="Credit Card",).save()

    VendorType(vendor_name="Walmart",).save()
    VendorType(vendor_name="Amazon",).save()
    VendorType(vendor_name="Costco/Sams",).save()
    VendorType(vendor_name="Starbucks",).save()


class Migration(migrations.Migration):

    replaces = [(b'admintool', '0001_initial'), (b'admintool', '0002_auto_20140921_0128'), (b'admintool', '0003_auto_20140922_0001'), (b'admintool', '0004_auto_20140922_0210'), (b'admintool', '0005_auto_20140923_1900'), (b'admintool', '0006_auto_20140924_2203')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount_spent', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='VendorType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vendor_name', models.CharField(max_length=25)),
                ('vendor_desc', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='expense',
            name='vendorType',
            field=models.ForeignKey(default=1, to='admintool.VendorType'),
            preserve_default=False,
        ),
        migrations.RunPython(
            code=load_data,
            reverse_code=None,
            atomic=True,
        ),
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
