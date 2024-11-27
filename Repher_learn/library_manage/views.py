from django.shortcuts import render

# Create your views here.
"""Permission checks in views and Templates"""
#1. VIEWS
def my_view(request):
    if request.user.has_perm('app_name.add_post'):
        #Allow user to create a anew post
        ...
    else:
        #Deny access or show an error message
        ...
    