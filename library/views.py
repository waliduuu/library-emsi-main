from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json


# Create your view
# here.

def login(request):
    context = {}
    return render(request, 'library/html/login.html', context)


def signup(request):
    context = {}
    return render(request, 'library/html/signup.html', context)


def myshelf(request):
    context = {}
    return render(request, 'library/html/myshelf.html', context)

def returnbook(request):
    context = {}
    render(request, 'library/html/return.html', context)


def history(request):
    context = {}
    render(request, 'library/html/history.html', context)




def home(request):
    books = book.objects.all()
    context = {'books':books}
    return render(request, 'library/html/home.html', context)



def shelf(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        emprunt, created = Emprunt.objects.get_or_create(customer=customer, complete=False)
        items = emprunt.empruntitem_set.all()
    else:
        items =[] 

    context = {'items':items}
    
    return render(request,'library/html/borrow.html', context )



def updateitem(request):
    data = json.loads(request.body)
    bookISBN = data['bookISBN']
    action = data['action']

    print('action', action)
    print('isbn', bookISBN)

    return JsonResponse('item was added', safe=False)