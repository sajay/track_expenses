from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template import Context,loader
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime 
from admintool.forms import ExpenseForm
from admintool.models import ExpenseCategory, ExpenseType, VendorType, Expense
from django.contrib.auth.decorators import login_required

# Create your views here.

def admin_view(request):
    return HttpResponse('<html><body>Admin Tool!</body></html>')

# This is a test view. Can be deleted.

def time_display(request):
    t = loader.get_template('time.html')
    c = Context({'current_time':datetime.now(),})
    return HttpResponse(t.render(c))

# Returns all expenses ordered by updated on

@login_required(login_url='/login')
def index(request):
    all_expenses = Expense.objects.filter(created_by=request.user).order_by('updated_on')
    t = loader.get_template('admintool/index.html')
    c = Context({'all_expenses':all_expenses,})
    return HttpResponse(t.render(c))


@login_required(login_url='/login')
def add_expense(request):
    errors =[]
    context = RequestContext(request)
 
    if request.method == "GET":
        form = ExpenseForm(request.GET)

        if form.is_valid():
            all_expenses = Expense.objects.filter(created_by=request.user).order_by('updated_on')
            expenseCategory = ExpenseCategory.objects.all()
            expenseType = ExpenseType.objects.all()
            vendorType = VendorType.objects.all()
            return render( request,  'add_expense.html' ,{'form':form, 'all_expenses':all_expenses, 'expenseCategory':expenseCategory, 'expenseType':expenseType, 'vendorType':vendorType} )  
        else:
            print form.errors
    else:
        form1=ExpenseForm()

    return render(request, 'add_expense.html' , {'errors':errors} )

@login_required(login_url='/login')

def save_expense(request):
    errors=[]
    if request.method == "POST":
        form=ExpenseForm(request.POST)
    else:
        form = ExpenseForm()
        return render (request, 'add_expense.html', {'form':form})
   
    expenseCategory = request.POST["expenseCategory"]
    expenseType = request.POST["expenseType"]
    vendorType = request.POST["vendorType"]
    expense_date = request.POST["expense_date"]
    amount_spent = request.POST["amount_spent"] 
    comments = request.POST["comments"]
    
    if len(expense_date) == 0  and len(amount_spent) == 0:
        messages.error(request, "Expense Date is a required field:" )
        messages.error(request, "Amount Spent is a required field:" )
        return render(request, 'add_expense.html', {'form':form}) 
    if len(expense_date) == 0:
        print "Into  expense_date is  None" 
        messages.error(request, "Expense Date is a required field:") 
        return render( request, 'add_expense.html', {'form':form})
    if len(amount_spent) == 0:  
        messages.error(request, "Amount Spent is a required field:" )
        return render( request, 'add_expense.html', {'form':form})
    if float(amount_spent) <=  0:
        messages.error(request, "Amount spent must be greater than zero") 
        return render( request, 'add_expense.html', {'form':form})

    datetime.datetime.strptime(expense_date,'%b %d, %Y')  
    ec=Expense(expenseCategory = ExpenseCategory(expenseCategory),
               expenseType = ExpenseType(expenseType) ,
               vendorType = VendorType( vendorType),
               expense_date =  datetime.datetime.strptime(expense_date,'%b %d, %Y') ,
               amount_spent = amount_spent , 
               comments = comments ,
               created_by = request.user)

    ec.save()
    messages.success( request, "Form data was saved successfully." )
    return HttpResponseRedirect(reverse(add_expense)) 



@login_required(login_url='/login')

def update_expense(request):
   
    id = request.POST["id"]
    expenseCategory = request.POST["expenseCategory"]
    expenseType = request.POST["expenseType"]
    vendorType = request.POST["vendorType"]
    expense_date = request.POST["expense_date"]
    amount_spent = request.POST["amount_spent"] 
    #comments = request.POST["comments"]
    try:
        exp = Expense.objects.get(pk=id)
    except ObjectDoesNotExist:
        return HttpResponse("Error, Could not find record for id : " + id   ) 
    
    if len(expense_date) == 0  and len(amount_spent) == 0:
        return HttpResponse( "Error,  <b>Expense Date</b>  and <b> Amount Spent</b> are required fields:"  )
    if len(expense_date) == 0:
        return HttpResponse( "Error, <b>Expense Date</b> is a required field:") 
    if len(amount_spent) == 0:  
        return HttpResponse( "Error, <b>Amount Spent</b> is a required field:" )
    if float(amount_spent) <=  0:
        return HttpResponse( "Error, <b>Amount spent</b> must be greater than zero:") 
    exp.expenseCategory = ExpenseCategory(expenseCategory)
    exp.expenseType = ExpenseType(expenseType)
    exp.vendorType = VendorType(vendorType)
    exp.expense_date = datetime.datetime.strptime(expense_date,'%b %d, %Y')  
    exp.amount_spent = amount_spent
    exp.created_by = request.user
    #exp.comments =  "TEST" 

    exp.save()
    return HttpResponse("Success, Expense Record has been updated successfully.")

@login_required(login_url='/login')
def delete_expense(request):
    print "Into delete_expense"
    id = request.POST["id"]
    print "Deleted Record is :" 
    print id
    try:
        exp = Expense.objects.get(pk=id)
    except ObjectDoesNotExist:
        return HttpResponse("Error, Could not find record for id : " + id   ) 
    exp.delete()      
    return HttpResponse("Success, Expense Record has been deleted successfully.")
