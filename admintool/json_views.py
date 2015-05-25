from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response  import Response 
from rest_framework import permissions
from admintool.models import ExpenseCategory, ExpenseType, VendorType, Expense, ExpenseTarget
from admintool.serializers import ExpenseSerializer,ExpenseCategorySerializer
from rest_framework import mixins, generics
from datetime import datetime

@api_view(['GET', 'POST'])
def expenseCategory_list(request):
     if request.method == 'GET':
        print "Into GET"
        ec  =ExpenseCategory.objects.all()
        serializer = ExpenseCategorySerializer(ec, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def expenseCategory_detail(request, pk):
    """
    Retrieve, update or delete a ExpenseCategory instance.
    """
    try:
        ec = ExpenseCategory.objects.get(pk=pk)
    except ExpenseCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ExpenseCategorySerializer(ec)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ExpenseCategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExpenseCollection(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Expense.objects.all() 
    serializer_class = ExpenseSerializer
    
    def get(self, request): 
        return self.list(request)
    
    def post(self, request): 
        return self.create(request)

class ExpenseDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
    
    queryset = Expense.objects.all() 
    serializer_class = ExpenseSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs): 
        return self.destroy(request, *args, **kwargs)


"""
 The view below filter expenses based on vendor type
ex:  http://127.0.0.1:8000/api/v1/expense/Walmart 
"""
@api_view(['GET', 'POST', 'DELETE'])
def expense_filterByVendor( request, vendor_name):
    try:
        print "Into expense_filterByVendor:"  
        print "Vendor Name is  :" + vendor_name
        vendor = VendorType.objects.filter( vendor_name=vendor_name) 
        exp = Expense.objects.filter(vendorType_id=vendor[0].id) 
    except Expense.DoesNotExist:    
        return Response( status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        serializer = ExpenseSerializer(exp, many=True) 
        return Response(serializer.data)

"""
  The view below filters expenses based on the month entered
ex: http://127.0.0.1:8000/api/v1/expense/2014/10   
"""
@api_view(['GET', 'POST', 'DELETE'])
def expense_filterByDate( request, yr, mth ):
    try:
        print "Into expense_filterByDate" 
        print "Year is :" + yr 
        print "Month is :" + mth 
#        exp = Expense.objects.filter(created_on__strftime("%Y%m" ) = yr_m ) 
        exp = Expense.objects.filter(expense_date__year=yr,expense_date__month=mth )
    except Expense.DoesNotExist:    
        return Response( status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        serializer = ExpenseSerializer(exp, many=True) 
        return Response(serializer.data)

"""
  The view below filters expenses based on year month and Vendor
ex : http://127.0.0.1:8000/api/v1/expense/2014/10/Walmart
"""
@api_view(['GET', 'POST', 'DELETE']) 
def expense_filterByDateVendor( request, yr, mth, vendor_name ):
    try:
        print "Into expense_filterByDateVendor" 
        print "Year is :" + yr 
        print "Month is :" + mth 
        print "Vendor is :" + vendor_name 
#        exp = Expense.objects.filter(created_on__strftime("%Y%m" ) = yr_m ) 
        vendor = VendorType.objects.filter(vendor_name=vendor_name)
        exp = Expense.objects.filter(expense_date__year=yr,expense_date__month=mth,  vendorType_id=vendor[0].id )
    except Expense.DoesNotExist:    
        return Response( status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        print "Into  Get" 
        serializer = ExpenseSerializer(exp, many=True) 
        return Response(serializer.data)


