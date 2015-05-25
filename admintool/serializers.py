from rest_framework import serializers
from admintool.models import Expense,ExpenseCategory, ExpenseType, VendorType

class ExpenseCategorySerializer( serializers.ModelSerializer):
    class Meta:
        model=ExpenseCategory
        fields=('id',  'category_name', 'category_desc' )

class ExpenseTypeSerializer( serializers.ModelSerializer):
    class Meta:
        model=ExpenseType
        fields=('id', 'type_name', 'type_desc' )

class VendorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=VendorType
        fields=('id' , 'vendor_name', 'vendor_desc')

class ExpenseSerializer( serializers.ModelSerializer):
    expenseCategory = serializers.RelatedField(source='ExpenseCategory')
    expenseType = serializers.RelatedField(source='ExpenseType')
    vendorType = serializers.RelatedField(source='VendorType')
    expCategory=serializers.RelatedField(source='expenseCategory.category_name')
    expType = serializers.RelatedField(source='expenseType.type_name')
    venType = serializers.RelatedField(source='vendorType.vendor_name')
    class Meta:
        model=Expense
        fields=('expCategory', 'expType','venType',  'amount_spent', 'expense_date') 
