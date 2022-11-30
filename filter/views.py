
from django.shortcuts import render
from usermanagement.models import receiptamount,weeklyloancreate
import dis

def receiptfilter(request):
    if request.method =="POST":
        name= request.POST.get('name')
        formdate= request.POST.get('formdate')
        todate= request.POST.get('todate')
        if name and formdate and todate :
            data = receiptamount.objects.filter(loan_name=name).filter(receipt_emi_date__range=[formdate,todate])
        elif name is  None:
            data=receiptamount.objects.filter(receipt_emi_date__range=[formdate,todate])
        elif formdate !="" and todate !="":
            data=receiptamount.objects.filter(loan_name=name)
        
        data1= weeklyloancreate.objects.all()
        total =0;
        for amount in data:
                sinle = amount.receipt_amount
                total = total + int(sinle)
               
        context={
                'obj':data,
                'data1':data1,
                'total':total,
            }
        return render(request,'receiptfilter.html',context)
    data = receiptamount.objects.all()
    data1= weeklyloancreate.objects.all()
    total =0;
    sinle=0;
    for amount in data:
                sinle = amount.receipt_amount
                total = total + int(sinle)
    context={
                'obj':data,
                'data1':data1,
                'total':total,
            }
    print("refes")
    return render(request,'receiptfilter.html',context)

def  loanfilter(request):
     data= weeklyloancreate.objects.all()
     total =0;
     data1=0;
     for amount in data:
                sinle = amount.weeklylan_amount
                sinlereceipt = amount.total_receipt_amount
                data1= data1 + int(sinlereceipt) 
                total = total + int(sinle)
     context={  
                'lone':data,
                'data1':data1,
                'total':total,
            }
     return render(request,'loanfilter.html',context)