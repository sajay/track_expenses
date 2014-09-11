from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def admin_view(request):
    return HttpResponse('<html><body>Admin Tool!</body></html>')
