from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response  import Response 
from rest_framework.permissions import *
from admintool.models import ExpenseCategory, ExpenseType, VendorType, Expense, ExpenseTarget
from admintool.serializers import ExpenseCategorySerializer


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

