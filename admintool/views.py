from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context,loader
from datetime import datetime
from admintool.models import Expense,ExpenseCategory,ExpenseType,VendorType

# Create your views here.

def admin_view(request):
    return HttpResponse('<html><body>Admin Tool!</body></html>')

# This is a test view. Can be deleted.

def time_display(request):
    t = loader.get_template('time.html')
    c = Context({'current_time':datetime.now(),})
    return HttpResponse(t.render(c))

# Returns all expenses ordered by updated on

def index(request):
    all_expenses = Expense.objects.all().order_by('updated_on')
    t = loader.get_template('admintool/index.html')
    c = Context({'all_expenses':all_expenses,})
    return HttpResponse(t.render(c))
