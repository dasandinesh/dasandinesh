from django.shortcuts import render,redirect
from adjustmentreceipt.models import creditadjustmentreceipt,deiptadjustmentreceipt,fineadjustment
from adjustmentreceipt.form import creditadjustmentreceiptform,deiptadjustmentreceiptform,fineadjustmentform

# Create your views here.
def creditadjustmentreceiptpage(request):
    if request.method =="POST":
        form = creditadjustmentreceiptform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/creditadjustmentreceiptpage')
    else:
        obj=creditadjustmentreceipt.objects.all()
        context={
            'form':creditadjustmentreceiptform,
            'obj':obj
        }
        return render(request,'creditadjustmentreceipt.html',context)
    return render(request,'creditadjustmentreceipt.html')

def deiptadjustmentreceiptpage(request):
    if request.method =="POST":
        form = deiptadjustmentreceiptform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/deiptadjustmentreceiptpage')
    else:
        obj=deiptadjustmentreceipt.objects.all()
        context={
            'form':deiptadjustmentreceiptform,
            'obj':obj
        }
        return render(request,'officenotifigation.html',context)
    return render(request,'officenotifigation.html')

def fineadjustmentpage(request):
    if request.method =="POST":
        form = fineadjustmentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/fineadjustmentpage')
    else:
        obj=fineadjustment.objects.all()
        context={
            'form':fineadjustmentform,
            'obj':obj
        }
        return render(request,'fineadjustment.html',context)
    return render(request,'fineadjustment.html')