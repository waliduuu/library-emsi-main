from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='homepage'),
    path('shelf/',views.shelf, name='shelfpage'),
    path('updateitem/',views.updateitem, name='updateitem'),
]