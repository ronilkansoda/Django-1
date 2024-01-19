from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    context = {
        'vari' : "This is omil"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is Home")

def about(request):
    return HttpResponse("This is About")

def services(request):
    return HttpResponse("This is Services")

def contact(request):
    return HttpResponse("This is Contact")