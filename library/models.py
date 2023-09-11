from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Class client
# # onetoonefield means that only one user per client 


# customer model 

class customer(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=30, null=True)
  email = models.CharField(max_length=200, null=True)
  profile_pic = models.ImageField(default="profilepic.png",null=True, blank=True)
# the return to see on the admin panel 

# return the user username related to the customer
  def __str__(self):
      return self.user.username



#model book
class Book(models.Model):
  title = models.CharField(max_length=30, null=True)
  author = models.CharField(max_length=30, null=True)
  category = models.CharField(max_length=30, null=True)
  ISBN = models.CharField(max_length=30, null=True)
  status = models.CharField(max_length=30, null=True)
  image = models.ImageField(null=True, blank=True)

  # return the book title

  def __str__(self):
    return self.title
  
  # if theres no image we add a blan so we dont get an error
  @property
  def imageURL(self):
    try:
        url = self.image.url
    except:
        url = ''
    return url
  



#book history
class BookHistory(models.Model):
  customer = models.ForeignKey(customer, on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
  starting_date = models.DateField(null=True, blank=True)

  # You can add more attributes as needed, like due date, fine amount, etc.

  def __str__(self):
      return self.customer.user.username+"'s new borrowing history"





  
      
  
#class emprunter
#on delete means if customer gets deleted the order stays with a null customer

class Emprunt(models.Model):
  customer = models.ForeignKey(customer, on_delete=models.SET_NULL,blank=True, null=True )
  transaction_id = models.CharField(max_length=200, null= True)
  complete = models.BooleanField(default=False, null=True, blank=False)
  date_emprunt = models.DateField(null=True)

  def __str__(self):
    if self.customer:
        return self.customer.name
    else:
        return "Unassigned Emprunt"
  
  @property
  def addy(self):
    addy = True
    return addy
  





 
class EmpruntItem(models.Model):
  book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
  emprunt = models.ForeignKey(Emprunt, on_delete=models.SET_NULL, blank=True, null=True)
  date_added = models.DateTimeField(auto_now_add=True)
  quantity = models.IntegerField(default=0, null=True, blank=True)

  def __str__(self):
    if self.emprunt and self.emprunt.customer:
        return self.emprunt.customer.name
    else:
        return "Unassigned Empruntitem"




class bookreturning(models.Model):
  customer = models.ForeignKey(customer, on_delete=models.SET_NULL,blank=True, null=True )
  book = models.ForeignKey(Book, on_delete=models.SET_NULL,blank=True, null=True )
  return_date = models.DateField(null=True, blank=True)

  def __str__(self):
    if self.customer.name:
        return self.customer.name
    else:
        return "Unassigned return"


