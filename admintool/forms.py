from django import forms
from admintool.models import ExpenseCategory, ExpenseType, VendorType, Expense

def clean_amount_spent(self):
    amount_spent = self.cleaned_data['amount_spent']
    if amount_spent <= 0:
        raise forms.ValidationError("Amount Spent must be greater than zero:" )
    return amount_spent 

class ExpenseForm(forms.Form):
    expenseCategory = forms.ModelChoiceField(label="Expense Category", queryset=ExpenseCategory.objects.all() , required=False )
    expenseType =  forms.ModelChoiceField(label="Expense Type", queryset=ExpenseType.objects.all(), required=False ) 
    vendorType =   forms.ModelChoiceField(label= "Vendor Type" , queryset=VendorType.objects.all(), required=False ) 
    expense_date = forms.DateField(label = "Expense Date",  required=False )
    amount_spent  = forms.DecimalField(label="Amount Spent" , required=False)
    comments =  forms.CharField(label="Comments" , required=False, widget=forms.Textarea)

    class Meta:
        model=Expense
        fields = ('expenseCategory', 'expenseType', 'vendorType', 'expense_date', 'amount_spent' ,  'comments' )
