from django.shortcuts import render
from .models import *


# Create your views here.

def login(request):
    context = {}
    return render(request, 'library/html/login.html', context)




def signup(request):
    context = {}
    return render(request, 'library/html/signup.html', context)




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

