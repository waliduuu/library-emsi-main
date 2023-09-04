from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json

from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user



# Create your view
# here.
@unauthenticated_user
def loginpage(request):

    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')


        customer = authenticate(request, username=Username, password=Password)

        if customer is not None:
            login(request,customer)
            return redirect('home')
        else:
            messages.info(request, 'username or password incorrect')
        

    context = {}
    return render(request, 'library/html/login.html', context)











def logoutUser(request):
    logout(request)
    return redirect('login')










@unauthenticated_user
def register(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            customer.objects.create(
                user=user,
            )

            messages.success(request, 'account was created for' + username)

            return redirect('login')


    context = {'form': form}
    return render(request, 'library/html/register.html', context)











@login_required(login_url='login')
def home(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        emprunt, created = Emprunt.objects.get_or_create(customer=customer, complete=False)
        items = emprunt.empruntitem_set.all()
    else:
        items =[] 
        emprunt = {'addy': False}

    context = {'items':items}        




    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'library/html/home.html', context)









@login_required(login_url='login')
def shelf(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        emprunt, created = Emprunt.objects.get_or_create(customer=customer, complete=False)
        items = emprunt.empruntitem_set.all()
    else:
        items =[] 
        emprunt = {'addy': False}

    context = {'items':items, 'emprunt': emprunt}
    
    return render(request,'library/html/myshelf.html', context)







@login_required(login_url='login')
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






@login_required(login_url='login')
def updatehistory(request): 

    data = json.loads(request.body)
    bookid = data['bookid']
    action = data['action']


    print(bookid)
    print(action)

    customer = request.user.customer
    book = Book.objects.get(id=bookid)
    emprunt, created = Emprunt.objects.get_or_create(customer=customer, complete=False)
    empruntitem, created = EmpruntItem.objects.get_or_create(emprunt=emprunt, book=book)
    history, created = BookHistory.objects.get_or_create(customer=customer, book=book)
    
    empruntitem.delete()
    emprunt.delete()
    history.save()
    return JsonResponse('item was added to history', safe=False)


def history(request):
    if request.user.is_authenticated:

        customer = request.user.customer
        historyitems = BookHistory.objects.filter(customer=customer)
    
    else:
        historyitems =[] 

    context = {'historyitems': historyitems}
    
    return render(request,'library/html/history.html', context)





def deleteitem(request):
    data = json.loads(request.body)
    bookid = data['bookid']
    action = data['action']

    print(bookid)
    print(action)

    customer = request.user.customer
    book = Book.objects.get(id=bookid)
    emprunt, created = Emprunt.objects.get_or_create(customer=customer, complete=False)

    try:
        empruntitem = EmpruntItem.objects.get(emprunt=emprunt, book=book)
        empruntitem.delete()
        return JsonResponse('Item was deleted', safe=False)
    except EmpruntItem.DoesNotExist:
        return JsonResponse('Item not found', status=404, safe=False)

    empruntitem.save()

    return JsonResponse('item was deleted', safe=False)













@login_required(login_url='login')
def account(request):
    context = {}
    return render(request, 'library/html/account.html', context)
















