from django.urls import path
from .views import pageUneVue

urlpatterns = [
    path('page1/',pageUneVue, name='pageune')
]