from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import datetime 
from admintool.forms import ExpenseForm
from admintool.models import ExpenseCategory, ExpenseType, VendorType, Expense

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

def add_expense(request):
    errors =[]
    context = RequestContext(request)
 
    if request.method == "GET":
        print "Into Http-GET" 
        form = ExpenseForm(request.GET)

        if form.is_valid():
      #      form.save(commit=True)
      #      return index(request)
            print "Form is valid"
            return render( request, 'add_expense.html', {'form':form})      

        else:
            print form.errors
    else:
        print "Form is not valid" 
        form1=ExpenseForm()

    return render(request, 'add_expense.html' , {'errors':errors} )

def save_expense(request):
    errors=[]
    form=ExpenseForm(request.POST)
    expenseCategory = request.POST["expenseCategory"]
    print expenseCategory
    expenseType = request.POST["expenseType"]
    print expenseType
    vendorType = request.POST["vendorType"]
    print vendorType
    expense_date = request.POST["expense_date"]
    print expense_date
   
    month,day ,year=expense_date.split('/')
    print day
    print month
    print year

    amount_spent = request.POST["amount_spent"] 
    print amount_spent

    ec=Expense(expenseCategory = ExpenseCategory(expenseCategory),expenseType = ExpenseType(expenseType) ,vendorType = VendorType( vendorType) ,expense_date = datetime.date(int(year), int(month), int(day))  , amount_spent = amount_spent )
     

    ec.save()
    return render( request,  'add_expense.html' ,{'errors':errors} )  

