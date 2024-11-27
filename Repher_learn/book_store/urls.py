from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path('hello/', views.hello_view, name='hello'),
    path('about', views.AboutView.as_view(), name='about'),
]