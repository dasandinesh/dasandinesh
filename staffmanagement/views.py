from django.shortcuts import render,redirect
from django.http import HttpResponse
from usermanagement.models import accounts, customer, pendingfine,receiptamount,sourcetype,EMItype,monthlyloancreate,weeklyloancreate,weeklydemand,updatedate
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        usernames=request.POST['username']
        passwords=username=request.POST['password']
        user =authenticate(request,username=usernames,password=passwords)
        if user is not None:
            auth_login(request,user)
            lastdate= updatedate.objects.get(id=1)
            data=weeklydemand.objects.filter(emi_demand_date=lastdate.last_update_date)
            penting =customer.objects.all()
            demand =weeklydemand.objects.all()
            context={
                'lastdate':lastdate,
                 'datas':data,
                'penting':penting,
                'demand':demand,
                }
            return render(request,'home.html',context)
        else:
            return HttpResponse("no users")
    return render(request,'login.html')

def logedout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
    else:
        form =UserCreationForm()

    return render(request,'register.html',{'form':form})
