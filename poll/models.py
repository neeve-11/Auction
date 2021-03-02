from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators

class user(AbstractUser):
     #models.UniqueConstraint(fields=['Username'], name='user_unique')
     email = models.EmailField(max_length=30, unique=True, validators=[validators.validate_email], error_messages ={'unique' : 'Email Id in not unique'} )
     first_name = models.CharField(max_length=30,)
     last_name = models.CharField(max_length=30)
class bidding(models.Model):
     CHOICES_CATEGORY = (
                          ("AI", "Antique Item"),
                          ("E", "Equipment"),
                          ("O", "Ornament"),
                          ("OT", "OTHERS")
                        )
     user = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, blank=True)
     name = models.CharField(max_length=40,null=True, default="aaa")
     price = models.IntegerField(null=True, default=000)
     picture = models.ImageField(null=True, default="nothing.jpeg", upload_to='itempic/')
     description = models.CharField(max_length=40, null=True, default="gehehe")
     catergory = models.CharField(max_length=2, null=True, default="OT", choices = CHOICES_CATEGORY)
class wishlist(models.Model):
     user = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, blank=True)
     item = models.ForeignKey(bidding, on_delete=models.SET_NULL,null=True,blank=True)
class comment(models.Model):
     user = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, blank=True)
     item = models.ForeignKey(bidding, on_delete=models.SET_NULL, null=True, blank=True)
     c_comment = models.CharField(max_length=40, null=True, blank=True)
