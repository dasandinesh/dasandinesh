from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
     path('login',views.login,name='login'),
     path('logedout',views.logedout,name='logedout'),
     path('register',views.register,name='register'),
]
