from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def dateinfo(request):
    date=datetime.datetime.now()
    msg='<h1> Hello Current Date and Time is:'+str(date)+'</h1>'
    return HttpResponse(msg)