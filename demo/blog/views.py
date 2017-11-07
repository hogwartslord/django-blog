from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect

# Create your views here.

def index(request):
    context = {'title':'test'}
    return render(request,'blog/index.html',context=context)

def hello(request):
    return HttpResponse('Hello World!')

def add(request,n1,n2):
    n1 = int(n1)
    n2 = int(n2)
    ret = '{} + {} = {}'.format(n1,n2,n1+n2)
    return HttpResponse(ret)

def mul(request):
    n1 = int(request.GET.get('n1'))
    n2 = int(request.GET.get('n2'))
    ret = '{} * {} = {}'.format(n1, n2, n1 * n2)
    return HttpResponse(ret)

def addtest(request):
    return HttpResponseRedirect('/blog/600/66/')
