from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from admintool import views
from django.shortcuts import render_to_response
from django.core.urlresolvers import resolve

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
        self.user = User.objects.create_user(
            username='testuser', email='testuser@test', password='secret')


    def test_root_resolves_to_main_view(self):
        main_page = resolve('/')
        self.assertEqual(main_page.func, views.index)

    def test_index_returns_correct_http_response_code(self):
        request = self.factory.get('/')
        request.user = self.user
        resp = views.index(request)
        self.assertEquals(resp.status_code, 200)

    
    def test_uses_index_html_template(self):
        request = self.factory.get('/')
        request.user = self.user
        
        #Make sure it has a session associated
        request.session = {} 

        
        #Call the view function
        response = views.index(request)
        
        #assertions
        self.assertContains(response, "<h1> Expense Incurred </h1>")

    def test_add_expense_resolves_to_add_view(self):
        add_expense_page = resolve('/add_expense/')
        self.assertEquals(add_expense_page.func, views.add_expense)

    def test_add_expense_returns_correct_http_response_code(self):
        request = self.factory.get('/add_expense/')
        request.user = self.user
        resp = views.add_expense(request)
        self.assertEquals(resp.status_code, 200)

    def test_uses_add_expense_html_template(self):
        #execute
        request = self.factory.get('/add_expense/')
        request.user = self.user
        request.session = {}
        
        #call the view
        response = views.add_expense(request)
        
        #assertions
        self.assertContains(response, "Add Your Expenses")
