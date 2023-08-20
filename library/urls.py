from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login, name='loginpage'),
    path('signup/',views.signup, name='signuppage'),
    path('home/',views.home, name='homepage'),
    path('shelf/',views.shelf, name='shelfpage'),
]