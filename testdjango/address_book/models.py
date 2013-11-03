from django.db import models

# Create your models here.

class AddressBookUser(models.Model):
    user_name = models.CharField(max_length=200)
    user_pwd = models.CharField(max_length=100)

