from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse("created a page")

def homeform(request):
    return render(request,'homeform.html')

def loginform(request):
    return render(request,'loginform.html')
    
def signupform(request):
    return render(request,'signupform.html')