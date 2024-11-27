from tokenize import group
from django.db import models

from book_store.models import User


# Create your models here.

# """
# ...WEEK 11 WORK...;
#  1.   Approaches to Customization
# """

# # 1. AbstractBaseUser
# from django.contrib.auth.models import AbstractBaseUser
# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=20)


# # 2. AbstractUser
# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     bio = models.TextField(blank = True)


"""
   2. Crafting Custom Authentication Backends
   ........Steps to implementation:.....
"""

# 1. define a custom backend class

from django.contrib.auth.backends import BaseBackend

class EmailBackend(BaseBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        return super().authenticate(request, username, password, **kwargs)
    #Implement logic to authenticate user using email and password

    def get_user(self, user_id):
        return super().get_user(user_id) 
    

"""
..............UNDERSTANDING PERMISSIONS AND GROUPS............
  
    
    1. Assaigning Permissions.
        (a)Through django admin interface.
"""
#(b)Programmatically
from django.contrib.auth.models import Permission
#Get permission
permission = Permission.objects.get(codename='add_post')

#Assign permission to a user
User.user_permissions.add(permission)

#Assign permission to a group
group.permissions.add(permission)