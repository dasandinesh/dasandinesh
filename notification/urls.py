from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('customernotification',views.customernotification,name='customernotification'), 
    path('officenotifigation',views.officenotifigation,name='officenotifigation'), 

]
