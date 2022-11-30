from usermanagement.models import customer, receiptamount, updatedate, weeklydemand, weeklyloancreate
from django.shortcuts import render

# Create your views here.
def receiptprintpage(requrest,id):
    receipt_info=receiptamount.objects.get(id=id)
    loanname=receipt_info.loan_name
    loan_info=weeklyloancreate.objects.get(weeklylan_loan_name=loanname)
    customername=receipt_info.customer_receipter_name
    customer_info=customer.objects.get(customer_name=customername)
    context={
        'loan_info':loan_info,
        'receipt_info':receipt_info,
        'customer_info':customer_info,
    }
    return render(requrest,'receiptprint.html',context)

def weeklydemandlistprint(requrest):
    lastupdated=updatedate.objects.get(id=1)
    weeklydemands=weeklyloancreate.objects.filter(weeklylan_date_demant=lastupdated.last_update_date)
    context={
        'weeklydemands':weeklydemands,
    }
    return render(requrest,'weeklydemandlistprint.html',context)

def monthlylistdemandprint(requrest):
    lastupdated=updatedate.objects.get(id=1)
    print()
    weeklydemands=weeklydemand.objects.filter(emi_demand_date=lastupdated.last_update_date)
    context={
        'weeklydemands':weeklydemands,
    }
    return render(requrest,'receiptprint.html',context)

def alldemandlistprint(requrest):
    alldemands=weeklyloancreate.objects.all()
    context={
        'alldemands':alldemands,
    }
    return render(requrest,'alldemandlistprint.html',context)

def allpendinglistprint(requrest):
    allpending=weeklydemand.objects.filter(pending_flag__gte=1)
    context={
        'allpending':allpending,
    }
    return render(requrest,'allpendinglistprint.html',context)

def receiptviewspage(requrest,id):
    receipt_info=receiptamount.objects.get(id=id)
    loanname=receipt_info.loan_name
    loan_info=weeklyloancreate.objects.get(weeklylan_loan_name=loanname)
    customername=receipt_info.customer_receipter_name
    customer_info=customer.objects.get(customer_name=customername)
    context={
        'loan_info':loan_info,
        'receipt_info':receipt_info,
        'customer_info':customer_info,
    }
    return render(requrest,'receiptviews.html',context)


def loaninfoprint(request,id):
    loan_info=weeklyloancreate.objects.get(id=id)
    cusname=loan_info.weeklylan_customer_name
    customer_info=customer.objects.get(customer_name=cusname)
    receipt_info=receiptamount.objects.filter(loan_name=loan_info.weeklylan_loan_name)
    
    context={
        'loan_info':loan_info,
        'receipt_info':receipt_info,
        'customer_info':customer_info,
    }
    return render(request,'loaninfoprint.html',context)