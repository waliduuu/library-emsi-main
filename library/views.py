from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json


# Create your view
# here.

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
    
    return render(request,'library/html/myshelf.html', context)

def confirmation(request):
    context = {}
    return render(request, 'library/html/confirmation.html', context)


def updateitem(request):
    data = json.loads(request.body)
    bookISBN = data['bookISBN']
    action = data['action']


    print(bookISBN)
    print(action)


    customer = request.user.customer
    book = book.objects.get(ISBN = bookISBN)
    emprunt, created = Emprunt.objects.get_or_create(customer=customer, complete=False)
    empruntItem, created = EmpruntItem.objects.get_or_create(emprunt=emprunt, book=book)


    return JsonResponse('item was added', safe=False)