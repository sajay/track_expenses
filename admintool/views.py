from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.template import Context,loader
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime 
import csv
from admintool.forms import ExpenseForm
import logging 
from admintool.forms import ExpenseForm
from admintool.models import ExpenseCategory, ExpenseType, VendorType, Expense, ExpenseTarget
from admintool.serializers import ExpenseCategorySerializer
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response  import Response 
from rest_framework.permissions import * 

from django.contrib.auth.models import User


logger=logging.getLogger(__name__)

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

# I  have written the two methods below to test the logging from the Django Shell. We can remove these after we have a grip on the logging framework.
def test_logging():
    print("name is : " + __name__)
    logger.debug("Test Logging, This is a debug message:" ) 

def test_logging_v1():
    logger.info( "Test Logging This is a info message:" ) 

@login_required(login_url='/login')
def add_expense(request):
    logger.info("Into add_expense():" )
    errors =[]
    context = RequestContext(request)
 
    if request.method == "GET":
        form = ExpenseForm(request.GET)

        if form.is_valid():
            #return render( request,  'admintool/add_expense.html' ,{'form':form, 'all_expenses':all_expenses, 'expenseCategory':expenseCategory, 'expenseType':expenseType, 'vendorType':vendorType} )             
            return render( request,  'admintool/add_expense.html' ,{'form':form,} )  
        else:
            print form.errors
    else:
        form1=ExpenseForm()

    return render(request, 'admintool/add_expense.html' , {'errors':errors} )

@login_required(login_url='/login')

def save_expense(request):
    logger.info("Into save_expense:" ) 
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
        return render(request, 'admintool/add_expense.html', {'form':form}) 
    if len(expense_date) == 0:
        print "Into  expense_date is  None" 
        messages.error(request, "Expense Date is a required field:") 
        return render( request, 'admintool/add_expense.html', {'form':form})
    if len(amount_spent) == 0:  
        messages.error(request, "Amount Spent is a required field:" )
        return render( request, 'admintool/add_expense.html', {'form':form})
    if float(amount_spent) <=  0:
        messages.error(request, "Amount spent must be greater than zero") 
        return render( request, 'admintool/add_expense.html', {'form':form})

    datetime.datetime.strptime(expense_date,'%b %d, %Y')
    ec=Expense(expenseCategory = ExpenseCategory(expenseCategory),
               expenseType = ExpenseType(expenseType) ,
               vendorType = VendorType( vendorType),
               expense_date =  datetime.datetime.strptime(expense_date,'%b %d, %Y') ,
               amount_spent = amount_spent , 
               comments = comments ,
               created_by = request.user)
    ec.save()
    messages.success( request, "The Expense was saved successfully." )
    return redirect('/expenses')
    #HttpResponseRedirect(reverse(index)) 
    #return render(request, 'admintool/index.html', {'form':form})


@login_required(login_url='/login')
@csrf_exempt
def update_expense(request):
  
    print "In Update"
    logger.info("Into update_expense() :" ) 
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
    logger.info("Into delete_expense() :" ) 
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
    logger.info("Into upload_target() :" ) 
    print "Into upload target"
    userName = None
    logger.info ("Into upload_target:" ) 
    if request.user.is_authenticated():
        userName = request.user.username
    print userName
    logger.info(userName)
    u = User.objects.get(username=userName) 
    if u == None:
        logger.info("User is not authenticated:" ) 
        messages.error(request, "User is not authenticated. Please login." )
    if request.method == "GET":
        print "Method is Get, Return back."
        logger.info("Into Method Get, Return back." )
        return render (request, 'admintool/upload_target.html')
    if request.method == "POST":
        print "Method is POST, process csv file:" 
        logger.info("Into method Post, process csv File:" ) 
        # if the file is not uploaded
        if not request.FILES:
            messages.error(request, "Please choose a file to upload:")
            return render( request, 'admintool/upload_target.html',)
        rowList= []
        errorList=[]
        file=request.FILES['targetfile']
        dataReader=csv.reader(file.read().splitlines())
        for row in dataReader:
            print "Into for loop :" 
            # Empty or incomplete file
            if len(row[0])==0 or len(row[1])==0 or len(row[2])==0 or len(row[3])==0:
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
                except MultipleObjectsReturned:
                    #if dupes exist
                    print "Adding to errorList"
                    errorList.append(row)
        #Iterate rowList and insert into DB
    for validRow in rowList:    
        print "Saving records to DB: " 
        target=ExpenseTarget( plan_type = validRow[0].strip(),  expenseCategory=ExpenseCategory(ec.id ), yr_m = validRow[2].strip(), amount=validRow[3], user=User(u.id) ) 
        target.save()  
    if len(rowList)> 0:
        print "Printing RowList:" 
        messages.success( request, "File uploaded successfully. Number of records uploaded:  " + str( len(rowList))  ) 
    if len(errorList) > 0:
        print "Printing ErrorList" 
        messages.error( request, str(len(errorList))  +  " Records did not load. Please correct "  ) 
    #return HttpResponseRedirect(reverse(upload_target)) 
    return render(request, 'admintool/upload_target.html',   )

@api_view(['GET', 'POST'])
def expenseCategory_list(request):
     if request.method == 'GET':
        print "Into GET"
        ec  =ExpenseCategory.objects.all()
        serializer = ExpenseCategorySerializer(ec, many=True)
        return Response(serializer.data)
