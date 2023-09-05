import django_filters


from .models import *

class Bookfilter(django_filters.FilterSet): 
    
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['image', 'ISBN']
