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
    return self.name


#class book
class book(models.Model):
  title = models.CharField(max_length=30, null=True)
  author = models.CharField(max_length=30, null=True)
  category = models.CharField(max_length=30, null=True)
  ISBN = models.CharField(max_length=30, null=True)
  status = models.BooleanField(default=True)
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

  def __str__(self):
    return str(self.id)
 
class EmpruntItem(models.Model):
  book = models.ForeignKey(book, on_delete=models.SET_NULL, blank=True, null=True)
  emprunt = models.ForeignKey(Emprunt, on_delete=models.SET_NULL, blank=True, null=True)
  date_debut_emprunt = models.DateField()

  
class bookreturning(models.Model):
  customer = models.ForeignKey(customer, on_delete=models.SET_NULL,blank=True, null=True )
  book = models.ForeignKey(book, on_delete=models.SET_NULL,blank=True, null=True )
  date_fin_emprunt = models.DateField()
  transaction_id = models.CharField(max_length=200, null= True)

  def __str__(self):
    return str(self.thereturn) 
