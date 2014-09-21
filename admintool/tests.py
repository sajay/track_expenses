from django.test import TestCase
from models import Expense
from datetime import date

# Create your tests here.

class ExpenseTests(TestCase):

    def test_values(self):
        expense = Expense(date=date.today(),amount_spent = 15.59)
        self.assertEquals(expense.date, date.today())
        self.assertEquals(str(expense.amount_spent), '15.59')
