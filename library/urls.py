from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login, name='loginpage'),
    path('signup/',views.signup, name='signuppage'),
    path('home/',views.home, name='homepage'),
    path('shelf/',views.shelf, name='shelfpage'),
    path('myshelf/',views.myshelf, name ='myshelfpage'),
    path('returnbook/',views.returnbook, name ='returnpage'),
    path('history/',views.history, name ='historypage'),
    path('updateitem/',views.updateitem, name ='updateitempage')
]