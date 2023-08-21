from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(customer)
admin.site.register(book)
admin.site.register(emprunt)
admin.site.register(bookreturning)
admin.site.register(itemtoemprunt)
