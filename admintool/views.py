from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context,loader
from datetime import datetime

# Create your views here.

def admin_view(request):
    return HttpResponse('<html><body>Admin Tool!</body></html>')

def time_display(request):
    t = loader.get_template('time.html')
    c = Context({'current_time':datetime.now(),})
    return HttpResponse(t.render(c))
