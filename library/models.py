from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Class client
# # onetoonefield means that only one user per client 
class customer(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=30, null=True)
  email = models.CharField(max_length=200, null=True)
# the return to see on the admin panel 
  def __str__(self):
    if self.name:
      return self.name
    return "Customer ID: {self.id}"


#class book
class Book(models.Model):
  title = models.CharField(max_length=30, null=True)
  author = models.CharField(max_length=30, null=True)
  category = models.CharField(max_length=30, null=True)
  ISBN = models.CharField(max_length=30, null=True)
  status = models.CharField(max_length=30, null=True)
  image = models.ImageField(null=True, blank=True)

  def __str__(self):
    return self.title
  
  @property
  def imageURL(self):
    try:
        url = self.image.url
    except:
        url = ''
    return url
      
  
#class emprunter
#on delete means if customer gets deleted the order stays with a null customer

class Emprunt(models.Model):
  customer = models.ForeignKey(customer, on_delete=models.SET_NULL,blank=True, null=True )
  transaction_id = models.CharField(max_length=200, null= True)
  complete = models.BooleanField(default=False, null=True, blank=False)
  date_emprunt = models.DateField(null=True)

  def __str__(self):
    return str(self.id)
  
  @property
  def addy(self):
    addy = True
    return addy
 
class EmpruntItem(models.Model):
  book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
  emprunt = models.ForeignKey(Emprunt, on_delete=models.SET_NULL, blank=True, null=True)
  date_added = models.DateTimeField(auto_now_add=True)
  quantity = models.IntegerField(default=0, null=True, blank=True)


class ConfirmationAdress(models.Model):
  customer = models.ForeignKey(customer, on_delete=models.SET_NULL,blank=True, null=True )
  emprunt = models.ForeignKey(Emprunt, on_delete=models.SET_NULL, blank=True, null=True)
  address = models.CharField(max_length=30, null=True)
  addressl2 = models.CharField(max_length=30, null=True)
  city = models.CharField(max_length=30, null=True)
  state = models.CharField(max_length=30, null=True)
  zipcode = models.CharField(max_length=30, null=True)
  date_added = models.DateTimeField(auto_now_add=True)



class bookreturning(models.Model):
  customer = models.ForeignKey(customer, on_delete=models.SET_NULL,blank=True, null=True )
  book = models.ForeignKey(Book, on_delete=models.SET_NULL,blank=True, null=True )
  date_fin_emprunt = models.DateField(auto_now_add=True)
  transaction_id = models.CharField(max_length=200, null= True)


  def __str__(self):
    return self.address


