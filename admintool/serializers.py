from rest_framework import serializers
from admintool.models import ExpenseCategory

class ExpenseCategorySerializer( serializers.ModelSerializer):
    class Meta:
        model=ExpenseCategory
        fields=('id',  'category_name', 'category_desc' )
   # pk = serializers.IntegerField(read_only=True)
   # category_name=serializers.CharField( required=True, max_length=25)
   # category_desc=serializers.CharField( required=False, max_length=50)

