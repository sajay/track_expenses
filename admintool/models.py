from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class ExpenseCategory( models.Model):
    category_name = models.CharField(max_length=25) 
    category_desc = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s ' % ( self.category_name, self.category_desc )
    
class ExpenseType( models.Model):
    type_name = models.CharField(max_length=25)
    type_desc = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' % ( self.type_name, self.type_desc )

class VendorType( models.Model):
    vendor_name = models.CharField(max_length=25)
    vendor_desc = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' % ( self.vendor_name,  self.vendor_desc )

class Expense(models.Model):
    #created_on : This is the default system date indicating when the expense was loaded into the system.

    #expense_date: This is the date when the actual  expense was incurred. This
    # date will  be of importance since all  queries will be based out of this
    # date

    expenseCategory = models.ForeignKey( ExpenseCategory)
    expenseType = models.ForeignKey ( ExpenseType )
    vendorType = models.ForeignKey ( VendorType)
    expense_date = models.DateField()
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.CharField(max_length=100)
    created_by = models.ForeignKey (User)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Expense " + str(self.expense_date)+ " Amount = " + str(self.amount_spent)

class ExpenseTarget(models.Model):
    plan_type = models.CharField(max_length=25)
    expenseCategory = models.ForeignKey( ExpenseCategory )
    yr_m = models.CharField( max_length=10 )
    amount = models.DecimalField( max_digits=10, decimal_places=2 )
#    user=models.CharField( max_length=25) 
    user = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
  
    def __unicode__(self):
        return "Expense Target " +  plan_type +  " Year month " + yr_m +  " Amount = " + str(self.amount)  
