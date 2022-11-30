from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'), 
    path('customerformpage',views.customerformpage,name='customerformpage'), 
    path('EMItypeformpage',views.EMItypeformpage,name='EMItypeformpage'), 
    path('sourcetypepage',views.sourcetypepage,name='sourcetypepage'), 
    path('receiptamountpage',views.receiptamountpage,name='receiptamountpage'), 
    path('customer/<int:id>',views.customerinfo,name='customerinfo'),
    path('weeklyloancreatepage',views.weeklyloancreatepage,name='weeklyloancreatepage'),
    path('monthlyloancreatepage',views.monthlyloancreatepage,name='monthlyloancreatepage'),
    path('monthlyintlist',views.monthlyintlist,name='monthlyintlist'),
    path('weeklyloanlist',views.weeklyloanlist,name='weeklyloanlist'),
    path('update',views.update,name='update'),
    path('demanddates',views.demanddates,name='demanddates'),
    path('pendinglist',views.pendinglist,name='pendinglist'),
    path('loaninformation/<str:weeklylan_loan_name>',views.loaninformation,name='loaninformation'),
    path('loannameautofill',views.loannameautofill,name='loannameautofill'),
    path('customernameautofill',views.customernameautofill,name='customernameautofill'),
    path('updatedays',views.updatedays,name='updatedays'),
    path('loanupdate',views.loanupdate,name='loanupdate'),
    path('qunitypriceupdate',views.qunitypriceupdate,name='qunitypriceupdate'),
    path('customerphonenumbersearch',views.customerphonenumbersearch,name='customerphonenumbersearch'),
    path('loanamozrtiondemo',views.loanamozrtiondemo,name='loanamozrtiondemo'),
]
