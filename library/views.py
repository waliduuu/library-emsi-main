from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json


# Create your view
# here.

def home(request):
    books = Book.objects.all()
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
    if request.user.is_authenticated:
        customer = request.user.customer
        emprunt, created = Emprunt.objects.get_or_create(customer=customer, complete=False)
        items = emprunt.empruntitem_set.all()
    else:
        items =[] 

    context = {'items':items, 'emprunt':emprunt,}

    return render(request, 'library/html/confirmation.html', context)


def updateitem(request):
    data = json.loads(request.body)
    bookid = data['bookid']
    action = data['action']


    print(bookid)
    print(action)

    customer = request.user.customer
    book = Book.objects.get(id=bookid)
    emprunt, created = Emprunt.objects.get_or_create(customer=customer, complete=False)

    empruntitem, created = EmpruntItem.objects.get_or_create(emprunt=emprunt, book=book)

    if action == 'add':
        empruntitem.quantity +=1
    elif action == 'remove':
        empruntitem.quantity -=1

    empruntitem.save()

    if empruntitem.quantity <= 0:
        empruntitem.delete()

    return JsonResponse('item was added', safe=False)