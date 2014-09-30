from django import forms
from admintool.models import ExpenseCategory, ExpenseType, VendorType, Expense

def clean_amount_spent(self):
    amount_spent = self.cleaned_data['amount_spent']
    if amount_spent <= 0:
        raise forms.ValidationError("Amount Spent must be greater than zero:" )
    return amount_spent 

class ExpenseForm(forms.Form):
    expenseCategory = forms.ModelChoiceField(queryset=ExpenseCategory.objects.all() , required=False )
    expenseType =  forms.ModelChoiceField(queryset=ExpenseType.objects.all(), required=False ) 
    vendorType =   forms.ModelChoiceField(queryset=VendorType.objects.all(), required=False ) 
    expense_date = forms.DateField( required=False )
    amount_spent  = forms.DecimalField(required=False)


    class Meta:
        model=Expense
        fields = ('expenseCategory', 'expenseType', 'vendorType', 'expense_date', 'amount_spent' )
