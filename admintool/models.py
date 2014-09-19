from django.db import models

# Create your models here.
class Expenses(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    amount_spent = models.DecimalField(max_digits=5, decimal_places=2)
