from django.contrib import admin

# Register your models here.
from admintool.models import ExpenseCategory
from admintool.models import ExpenseType
from admintool.models import VendorType
from admintool.models import Expense

admin.site.register(ExpenseCategory)
admin.site.register(ExpenseType)
admin.site.register(VendorType)
admin.site.register(Expense)
