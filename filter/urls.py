from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('receiptfilter',views.receiptfilter,name='receiptfilter'),
    path('loanfilter',views.loanfilter,name='loanfilter'),  
]
