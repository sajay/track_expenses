from django.db import models

# Create your models here.
class Expense(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    amount_spent = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return "Expense " + str(self.date) + " Amount = " + str(self.amount_spent)
