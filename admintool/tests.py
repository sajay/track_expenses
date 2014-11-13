from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from admintool import views
from django.shortcuts import render_to_response
from django.core.urlresolvers import resolve
from django.views.generic import TemplateView
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


    def test_root_url_resolves_to_home_page(self):
        home = resolve('/')

        # Setup name.
        name = 'home'
        # Setup request and view.
        request = self.factory.get('/')
        view = TemplateView.as_view(template_name='homepage.html')
        # Run.
        response = view(request,name=name)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'homepage.html')
        self.assertEqual(response.context_data['name'], name)




    def test_expenses_resolves_to_main_expenses_list(self):
        main_page = resolve('/expenses/')
        self.assertEqual(main_page.func, views.index)

    def test_index_returns_correct_http_response_code(self):
        request = self.factory.get('/expenses/')
        request.user = self.user
        resp = views.index(request)
        self.assertEquals(resp.status_code, 200)


    def test_uses_index_html_template(self):
        request = self.factory.get('/expenses/')
        request.user = self.user

        #Make sure it has a session associated
        request.session = {}


        #Call the view function
        response = views.index(request)

        #assertions
        self.assertContains(response, "<h1> Expenses List </h1>")

    def test_call_to_root_view_denies_anonymous(self):
        resp = self.client.get('/expenses/', follow=True)
        self.assertEquals(resp.redirect_chain[0][0],'http://testserver/login?next=/expenses/')
        self.assertEquals(resp.redirect_chain[0][1],302)



    def test_add_expense_resolves_to_add_view(self):
        add_expense_page = resolve('/expenses/add/')
        self.assertEquals(add_expense_page.func, views.add_expense)

    def test_add_expense_returns_correct_http_response_code(self):
        request = self.factory.get('expenses/add')
        request.user = self.user
        resp = views.add_expense(request)
        self.assertEquals(resp.status_code, 200)

    def test_uses_add_expense_html_template(self):
        #execute
        request = self.factory.get('/expenses/add/')
        request.user = self.user
        request.session = {}

        #call the view
        response = views.add_expense(request)

        #assertions
        self.assertContains(response, "Add Expenses")

    def test_call_to_add_expense_view_denies_anonymous(self):
        resp = self.client.get('/expenses/add/', follow=True)

        self.assertEquals(resp.redirect_chain[0][0],'http://testserver/login?next=/expenses/add/')
        self.assertEquals(resp.redirect_chain[0][1],302)

    def test_call_to_add_expense_posts_expense(self):
        request = self.factory.get('expenses/add')
        request.user = self.user
        request.method = "POST"
        request.POST['expenseCategory'] = "Groceries"
        request.POST['expenseType'] = "Cash"
        request.POST['vendorType'] = "Walmart"
        request.POST['expense_date'] = "Apr 02, 2014"
        request.POST['amount_spent'] = "1234"
        request.POST['comments'] = "Test expense Unit Test"
        
        response = views.save(request)

        self.assertIn("Test expense Unit Test",response.content.decode())


