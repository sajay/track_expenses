from django import forms
from admintool.models import ExpenseCategory, ExpenseType, VendorType, Expense,ExpenseTarget

def clean_amount_spent(self):
    print "Into clean_amount_spent" 
    amount_spent = self.cleaned_data['amount_spent']
    if amount_spent <= 0:
        raise forms.ValidationError("Amount Spent must be greater than zero:" )
    return amount_spent 

def clean_expense_date(self):
    print "Into clean_expense_date" 
    expense_date = self.cleaned_date['expense_date']
    if expense_date is None:
        raise forms.ValidationError("Expense Date cannot be blank:")
    return expense_date	

class ExpenseForm(forms.Form):
    expenseCategory = forms.ModelChoiceField(label="Expense Category", queryset=ExpenseCategory.objects.all() , required=False, empty_label=None )
    expenseType =  forms.ModelChoiceField(label="Expense Type", queryset=ExpenseType.objects.all(), required=False, empty_label=None ) 
    vendorType =   forms.ModelChoiceField(label= "Vendor Type" , queryset=VendorType.objects.all(), required=False,  empty_label=None ) 
    expense_date = forms.DateField(label = "Expense Date",  required=False )
    amount_spent  = forms.DecimalField(label="Amount Spent" , required=False)
    comments =  forms.CharField(label="Comments" , required=False, widget=forms.Textarea)

    class Meta:
        model=Expense
        fields = ('expenseCategory', 'expenseType', 'vendorType', 'expense_date', 'amount_spent' ,  'comments' )

class UploadFileForm(forms.Form):
    targetfile=forms.FileField()
 
    class Meta:
        model=ExpenseTarget
        fields=('targetfile')
