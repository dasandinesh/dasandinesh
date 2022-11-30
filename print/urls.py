from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
     path('receipt/<int:id>',views.receiptprintpage,name='receiptprintpage'), 
     path('weeklydemandlistprint',views.weeklydemandlistprint,name='weeklydemandlistprint'), 
     path('alldemandlistprint',views.alldemandlistprint,name='alldemandlistprint'), 
     path('allpendinglistprint',views.allpendinglistprint,name='allpendinglistprint'),
     path('receiptviewspage/<int:id>',views.receiptviewspage,name='receiptviewspage'), 
     path('loaninfoprint/<int:id>',views.loaninfoprint,name='loaninfoprint'),
]
