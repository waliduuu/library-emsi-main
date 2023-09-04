from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('myshelf/',views.shelf, name='myshelf'),
    path('confirmation/',views.confirmation, name='confirmation'),
    path('update_item/',views.updateitem, name='update-item'),
    path('delete_item/',views.deleteitem, name='delete-item'),
    path('account/',views.account, name='account'),
    path('history/',views.history, name='history'),
    path('login/',views.loginpage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.register, name='register'),

]