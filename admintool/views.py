from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template import Context,loader
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime 
import csv
from admintool.forms import ExpenseForm, UploadFileForm
from admintool.models import ExpenseCategory, ExpenseType, VendorType, Expense, ExpenseTarget
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#Delete This too

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
    expenseCategory = ExpenseCategory.objects.all()
    expenseType = ExpenseType.objects.all()
    vendorType = VendorType.objects.all()
 
    t = loader.get_template('admintool/index.html')
    c = Context({'all_expenses':all_expenses,'expenseCategory':expenseCategory, 'expenseType':expenseType,'vendorType':vendorType })
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
            return render( request,  'admintool/add_expense.html' ,{'form':form, 'all_expenses':all_expenses, 'expenseCategory':expenseCategory, 'expenseType':expenseType, 'vendorType':vendorType} )  
        else:
            print form.errors
    else:
        form1=ExpenseForm()

    return render(request, 'admintool/add_expense.html' , {'errors':errors} )

@login_required(login_url='/login')

def save_expense(request):
    errors=[]
    if request.method == "POST":
        form=ExpenseForm(request.POST)
    else:
        form = ExpenseForm()
        return render (request, 'admintool/add_expense.html', {'form':form})
   
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
    return HttpResponseRedirect(reverse(index)) 



@login_required(login_url='/login')
@csrf_exempt
def update_expense(request):
  
    print "In Update"
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
@csrf_exempt
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

@login_required(login_url='/login')
def upload_target(request):
    print "Into upload target"
    if request.method == "GET":
        print "Method is Get, Return back."
        return render (request, 'upload_target.html')
    if request.method == "POST":
        print "Method is POST, process csv file:" 
        form=UploadFileForm(request.POST, request.FILES) 
        rowList= []
        errorList=[]
        file=request.FILES['targetfile']
       # if file is None :
       #     messages.error(request, "Please choose a file to upload:") ) 
       #     return render( request, 'upload_target.html', {'form':form})
        dataReader=csv.reader(file.read().splitlines())
        for row in dataReader:
            print "Into for loop :" 
            if len(row[0])==0 or len(row[1])==0 or len(row[2])==0 or len(row[3])==0 or len(row[4]) == 0 :
               errorList.append(row)
            # Get expenseCategory_id from the ExpenseCategory value.
            else:
                try: 
                    ec = ExpenseCategory.objects.get(category_name  = row[1].strip() )
                except ObjectDoesNotExist:
                    # Add to  errorList
                    errorList.append(row) 
                    break  # Get out of the else block.
                print "ec.id is :" + str(ec.id  ) 
                try:
                    # Check whether the record has already been uploaded. 
                    et=ExpenseTarget.objects.get(plan_type=row[0].strip(), expenseCategory_id=ec.id, yr_m=row[2].strip())
                    if et:
                        #Record already  exists
                        print "Expense Target object already  exists" 
                        errorList.append(row) 
                except ObjectDoesNotExist:    
                    #record needs to be inserted into ExpenseTarget
                    # Insert into pristineList
                    print "Adding to  rowlist :" 
                    rowList.append(row)  

        #Iterate rowList and insert into DB
    for validRow in rowList:    
        print "Saving records to DB: " 
        target=ExpenseTarget( plan_type = validRow[0].strip(),  expenseCategory=ExpenseCategory(ec.id ), yr_m = validRow[2].strip(), amount=validRow[3], user=validRow[4] ) 
        target.save()  
    if len(rowList)> 0:
        print "Printing RowList:" 
        messages.success( request, "File uploaded successfully. Number of records uploaded:  " + str( len(rowList))  ) 
    if len(errorList) > 0:
        print "Printing ErrorList" 
        messages.error( request, str(len(errorList))  +  " Records did not load. Please correct "  ) 
    #return HttpResponseRedirect(reverse(upload_target)) 
    return render(request, 'upload_target.html', {'form':form}   )
