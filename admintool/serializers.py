from rest_framework import serializers
from admintool.models import Expense,ExpenseCategory

class ExpenseCategorySerializer( serializers.ModelSerializer):
    class Meta:
        model=ExpenseCategory
        fields=('id',  'category_name', 'category_desc' )
   # pk = serializers.IntegerField(read_only=True)
   # category_name=serializers.CharField( required=True, max_length=25)
   # category_desc=serializers.CharField( required=False, max_length=50)

class ExpenseSerializer( serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields=('id','expenseCategory','expenseType','amount_spent','vendorType')

