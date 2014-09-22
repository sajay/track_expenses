from django.db import models
# Create your models here.

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
    #date : This is the default system date indicating when the expense was     #loaded into the system.

    #expense_date: This is the date when the actual  expense was incurred. This
    # date will  be of importance since all  queries will be based out of this d    #ate

    expenseCategory = models.ForeignKey( ExpenseCategory)
    expenseType = models.ForeignKey ( ExpenseType )
    vendorType = models.ForeignKey ( VendorType)
    date = models.DateTimeField(auto_now_add=True)
    expense_date = models.DateField()
    amount_spent = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return "Expense " + str(self.date) + " Amount = " + str(self.amount_spent)
  
