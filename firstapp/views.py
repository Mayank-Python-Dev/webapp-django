from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request, 'index.html',{'name':'World'})

def add(request):

    x = int(request.POST['num1'])
    y = int(request.POST['num2'])
    res = x + y

    return render(request,'result.html',{'result': res})