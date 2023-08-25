from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(customer)
admin.site.register(book)
admin.site.register(Emprunt)
admin.site.register(bookreturning)
admin.site.register(EmpruntItem)
