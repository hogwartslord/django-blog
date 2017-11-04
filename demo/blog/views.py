from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'blog/index.html')

def hello(request):
    return HttpResponse('Hello World!')

def add(request,num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    ret = '{} + {} = {}'.format(num1,num2,num1+num2)
    return HttpResponse(ret)



