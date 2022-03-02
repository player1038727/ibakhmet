from django.shortcuts import render
from django.http import HttpResponse

#from .models import Greeting

# Create your views here.
def x(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "x.html")


