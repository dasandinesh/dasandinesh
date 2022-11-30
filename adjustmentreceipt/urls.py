from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('creditadjustmentreceiptpage',views.creditadjustmentreceiptpage,name='creditadjustmentreceiptpage'), 
    path('deiptadjustmentreceiptpage',views.deiptadjustmentreceiptpage,name='deiptadjustmentreceiptpage'), 
    path('fineadjustmentpage',views.fineadjustmentpage,name='fineadjustmentpage'),  
]
