from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('myshelf/',views.shelf, name='myshelf'),
    path('confirmation/',views.confirmation, name='confirmation'),
]