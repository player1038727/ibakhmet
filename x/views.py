from django.shortcuts import render
from django.http import HttpResponse
#import requests


#from .models import Greeting

# Create your views here.
def x(request):
    # return HttpResponse('Hello from Python!')
    context = '1'
    return render(request, "x.html", context)


