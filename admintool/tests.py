from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from admintool import views
#from models import Expense
#from datetime import date

# Create your tests here.

class AdminToolTests(TestCase):

    #def test_values(self):
    #    expense = Expense(date=date.today(),amount_spent = 15.59)
    #    self.assertEquals(expense.date, date.today())
    #    self.assertEquals(str(expense.amount_spent), '15.59')

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user1 = User.objects.create_user(
            username='testuser1', email='testuser@test', password='secret')
        self.user2 = User.objects.create_user(
            username='testuser2', email='testuser@test', password='secret')

    def test_uses_index_html_template(self):
        request = self.factory.get('/')
        request.user = self.user1
        
        #Make sure it has a session associated
        request.session = {} 

        
        #Call the view function
        response = views.index(request)
        
        #assertions
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1> Expense Incurred </h1>")
    
    def test_uses_add_expense_html_template(self):
        #execute
        request = self.factory.get('/add_expense/')
        request.user = self.user2
        request.session = {}
        
        #call the view
        response = views.add_expense(request)
        
        #assertions
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add Your Expenses")
