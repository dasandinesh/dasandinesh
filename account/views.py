from django.shortcuts import render
from usermanagement.models import customer
from adjustmentreceipt.models import creditadjustmentreceipt,deiptadjustmentreceipt,fineadjustment

def account(request):
    context={

    }
    return render(request,'account.html',context)