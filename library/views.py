from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def login(request):
    context = {}
    return render(request, 'library/html/login.html', context)
def signup(request):
    context = {}
    return render(request, 'library/html/signup.html', context)
def home(request):
    context = {}
    return render(request, 'library/html/home.html', context)
def shelf(request):
    context = {}
    return render(request,'library/html/borrow.html', context )

