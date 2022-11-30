from django.db.models import query
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from usermanagement.models import accounts, customer, pendingfine,receiptamount,sourcetype,EMItype,monthlyloancreate,weeklyloancreate,weeklydemand,updatedate
from usermanagement.form import customerform,receiptamountform,sourcetypeform,EMItypeform,monthlyloancreateform,weeklyloancreateform
from datetime import datetime, timedelta
from datetime import date
import time    
from django.contrib.auth.decorators import login_required
  

# Create your views here.
@login_required(login_url='/login')
def home(request):
    lastdate= updatedate.objects.get(id=1)
    data=weeklyloancreate.objects.filter(weeklylan_date_demant=lastdate.last_update_date)
    penting =customer.objects.all()
    demand =weeklyloancreate.objects.all()
    context={
        'lastdate':lastdate,
        'datas':data,
        'penting':penting,
        'demand':demand,
    }
    return render(request,'home.html',context)

def update(request):
    lastupdatedate=updatedate.objects.get(id=1)
    if date.today() <= lastupdatedate.last_update_date:
       context={
           'todaydate':date.today(),
           'update':lastupdatedate.last_update_date,
       }
    else :
        yesterday = date.today() 
        cuslist =weeklyloancreate.objects.filter(weeklylan_date_demant=lastupdatedate.last_update_date)#get yesteday data
        for cus in cuslist:#dateincrec based on emi datas
            print(cus.weeklylan_customer_name)
            emitype=EMItype.objects.get(EMItype_name=cus.weeklylan_EMItype) 
            cus.weeklylan_date_demant = (lastupdatedate.last_update_date + timedelta(days=emitype.EMI_daylength))
            cus.pending_flag= cus.pending_flag + int(1)
            cus.save()
        cus_pent_list = weeklyloancreate.objects.filter(pending_flag__gte=1)
        for pent in cus_pent_list:#add fine
            print(pent.weeklylan_customer_name)
            fine_t_a = pent.total_fine_amount
            pent.total_fine_amount = fine_t_a + pent.per_day_fine
            pent.save()
        lastupdatedate.last_update_date = lastupdatedate.last_update_date + timedelta(days=1)
        lastupdatedate.save()
        context={
           'todaydate':date.today(),
           'update':lastupdatedate.last_update_date,
       }
    return render(request,'updatedays.html',context)

@login_required(login_url='/login')
def customerformpage(request):
    if request.method =="POST":
        customer_name= request.POST.get('customer_name')
        customer_dateofbirth= request.POST.get('customer_dateofbirth')
        sex= request.POST.get('sex')
        phone= request.POST.get('phone')
        community= request.POST.get('community')
        Doorno= request.POST.get('Doorno')
        street_name= request.POST.get('street_name')
        area_name= request.POST.get('area_name')
        finance_amount= request.POST.get('finance_amount')
        paid_amount= request.POST.get('paid_amount')
        pending_amount= request.POST.get('pending_amount')
        acnumber= request.POST.get('acnumber')
        ifsc= request.POST.get('ifsc')
        bankname= request.POST.get('bankname')
        brach= request.POST.get('brach')
        pannumber= request.POST.get('pannumber')
        occupations= request.POST.get('occupations')
        idproof= request.POST.get('idproof')
        photo= request.POST.get('photo')
        account = customer(customer_name=customer_name,customer_dateofbirth=customer_dateofbirth,customer_sex=sex,customer_phone=phone,customer_community=community,customer_Doorno=Doorno,customer_street_name=street_name,customer_area_name=area_name,customer_finance_amount=finance_amount,customer_paid_amount=paid_amount,customer_pending_amount=pending_amount,customer_acnumber=acnumber,customer_ifsc=ifsc,customer_bankname=bankname,customer_brach=brach,customer_pannumber=pannumber,customer_occupations=occupations,customer_idproof=idproof,customer_photo=photo,pending_flag=0)
        account.save(force_insert=True)
        return redirect('customerformpage')
    else:
        obj=customer.objects.all()
        context={
            'form':customerform,
            'obj':obj
        }
        return render(request,'customercreateentry.html',context)

@login_required(login_url='/login')
def EMItypeformpage(request):
    if request.method =="POST":
        form = EMItypeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('EMItypeformpage')
    else:
        obj=EMItype.objects.all()
        context={
            'form':EMItypeform,
            'obj':obj
        }
        return render(request,'emitype.html',context)

@login_required(login_url='/login')
def receiptamountpage(request):
    if request.method =="POST":
        customername= request.POST.get('customername')
        loanname= request.POST.get('loanname')
        fromdate= request.POST.get('from')
        amount= request.POST.get('amount')
        discretion= request.POST.get('discretion')
        account = receiptamount(customer_receipter_name=customername,loan_name=loanname,receipt_emi_date=fromdate,receipt_amount=amount,receipt_discretion=discretion)
        weeklydemand.objects.filter(weeklydemand_loan_name=loanname).update(pending_flag=-1)
        account.save(force_insert=True)
        weeklyloancreates= weeklyloancreate.objects.get(weeklylan_loan_name=loanname)
        weeklyloanreciptamount=weeklyloancreates.total_receipt_amount + int(amount)
        weeklyloancreate.objects.filter(weeklylan_loan_name=loanname).update(total_receipt_amount=weeklyloanreciptamount)
        return redirect('/receiptamountpage')
    else:
        obj=reversed(receiptamount.objects.all())
        context={
            'form':receiptamountform,
            'obj':obj
        }
        return render(request,'receiptamountentry.html',context)

@login_required(login_url='/login')
def sourcetypepage(request):
    if request.method =="POST":
        form = sourcetypeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sourcetypepage')
    else:
        obj=sourcetype.objects.all()
        context={
            'form':sourcetypeform,
            'obj':obj
        }
        return render(request,'source.html',context)

def customerinfo(request,id):
    data = customer.objects.get(id=id)
    list= weeklyloancreate.objects.filter(weeklylan_customer_name=data.customer_name)
    dates =data.customer_createdate + timedelta(days=60)
    context={
        'dates':dates,
        'customerinfos':data,
        'list':list
    }
    return render(request,'customerinfo.html',context)


def weeklyloanlist(request):
        obj=weeklyloancreate.objects.all()
        context={
            'obj':obj,
        }
        return render(request,'weeklyloanlist.html',context)


@login_required(login_url='/login')
def weeklyloancreatepage(request):
    if request.method =="POST":
        name= request.POST.get('name')
        loanname= request.POST.get('loanname')
        EMItypes= request.POST.get('EMItype')
        sourcetypes= request.POST.get('sourcetype')
        firstemidate= request.POST.get('firstemidate')
        amount= request.POST.get('amount')
        totalweek= request.POST.get('totalweek')
        weeklyEMI= request.POST.get('weeklyEMI')
        per_day_fines=request.POST.get('per_day_fine')
        loantype=request.POST.get('loantype')
        autofinace=request.POST.get('autofinace')
        homefinace=request.POST.get('homefinace')
        prof=request.POST.get('prof')
        loanphone=request.POST.get('loanphone')
        account = weeklyloancreate(weeklylan_customer_name=name,weeklylan_loan_name=loanname,weeklylan_EMItype=EMItypes,weeklylan_sourcetype=sourcetypes,weeklylan_date_demant=firstemidate,weeklylan_amount=amount,weeklylan_totalweek=totalweek,weeklylan_weeklyEMI=weeklyEMI,per_day_fine=per_day_fines,pending_flag=0,total_receipt_amount=0,total_fine_amount=0,lone_type=loantype,autofinace=autofinace,homeloanifo=homefinace,prof=prof,loan_phone_no=loanphone)
        account.save(force_insert=True)
        accounts2 = weeklydemand(weeklydemand_loan_name=loanname,emi_amount=weeklyEMI,emi_demand_date=firstemidate,pending_flag=0)
        accounts2.save(force_insert=True)
        customer.objects.filter(customer_name=name).update(customer_finance_amount=amount)
        return redirect('weeklyloancreatepage')
    else:
        obj=weeklyloancreate.objects.all()
        EMItypess=EMItype.objects.all()
        sourcetypess=sourcetype.objects.all()
        customerdt=customer.objects.all()
        context={
            'EMItypes':EMItypess,
            'sourcetypes':sourcetypess,
            'form':weeklyloancreateform,
            'obj':obj,
            'customerdt':customerdt,
        }
    return render(request,'weeklyloanpage.html',context)

@login_required(login_url='/login')
def monthlyloancreatepage(request):
    if request.method =="POST":
        form = monthlyloancreateform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("error")
        return redirect('monthlyloancreatepage')
    else:
        obj=monthlyloancreate.objects.all()
        context={
            'obj':obj,
            'form':monthlyloancreateform
        }
        return render(request,'monthlyloanpage.html',context)

def monthlyintlist(request):
        obj=monthlyloancreate.objects.all()
        context={
            'obj':obj,
        }
        return render(request,'monthlyintlist.html',context)

def demanddates(request):
    data =weeklydemand.objects.all()
    context={
        'datas':data,
    }
    return render(request,'demanddates.html',context)

def pendinglist(request):
    data =customer.objects.all()
    context={
        'datas':data,
    }
    return render(request,'pendinglist.html',context)


def loaninformation(request,weeklylan_loan_name):
    receiptsforloan=receiptamount.objects.filter(loan_name=weeklylan_loan_name)
    loan= weeklyloancreate.objects.get(weeklylan_loan_name=weeklylan_loan_name)
    customers=customer.objects.get(customer_name=loan.weeklylan_customer_name)
    fine=pendingfine.objects.filter(fine_customer=weeklylan_loan_name)

    context={
        'receiptsforloan':receiptsforloan,
        'loan':loan,
        'customers':customers,
        'fine':fine,
    }
    return render(request,'loaninformation.html',context)

def loannameautofill(request):
    query_original = request.GET.get('term')
    un = list(weeklyloancreate.objects.filter(weeklylan_loan_name__icontains=query_original).values())
    return JsonResponse(un,safe=False)

def customernameautofill(request):
    query_original = request.GET.get('term')
    un = list(customer.objects.filter(customer_name__icontains=query_original).values())
    return JsonResponse(un,safe=False)

def updatedays(request):
    updates=weeklyloancreate.objects.filter(pending_flag__gte = 1)
    lastupdate=updatedate.objects.filter(id=1)
    context={
        'updates':updates,
        'lastupdate':lastupdate,
    }
    return render(request,'updatedays.html',context)

def loanupdate(request):
    query_original = request.GET.get('data')
    data =list(weeklyloancreate.objects.filter(id=query_original).values())
    return JsonResponse(list(data),safe=False)

def qunitypriceupdate(request):
    if request.method == 'POST':
        id= request.POST.get('id', None)
        loanname= request.POST.get('loanname', None)
        Customername = request.POST.get('Customername', None)
        demantdate = request.POST.get('demantdate', None)
        totalamount = request.POST.get('totalamount', None)
        totalweek = request.POST.get('totalweek', None)
        emiamount = request.POST.get('emiamount', None)
        dayfine = request.POST.get('dayfine', None)
        pending = request.POST.get('pending', None)
        paidamount = request.POST.get('paidamount', None)
        fine = request.POST.get('fine', None)
        if loanname and Customername and demantdate and totalamount and totalweek and emiamount and dayfine and pending and paidamount and fine: #cheking if first_name and last_name have value
           weeklyloancreate.objects.filter(id=id).update(weeklylan_customer_name=Customername,weeklylan_loan_name=loanname,weeklylan_date_demant=demantdate,weeklylan_amount=totalamount,weeklylan_totalweek=totalweek,weeklylan_weeklyEMI=emiamount,per_day_fine=dayfine,pending_flag=pending,total_receipt_amount=paidamount,total_fine_amount=fine)
           return HttpResponse("response")
        else:
            print(id,loanname,Customername,demantdate,totalamount,totalweek,emiamount,dayfine,pending,
            paidamount,fine)
    return HttpResponse("response")

def customerphonenumbersearch(request):
    
    query_original = request.GET.get('term')
    if query_original != "":
        un = list(weeklyloancreate.objects.filter(loan_phone_no__icontains=2147483647).values())
        return JsonResponse(un,safe=False)
    else:
        un = list(weeklyloancreate.objects.filter(loan_phone_no__icontains=query_original).values())
        return JsonResponse(un,safe=False)


def loanamozrtiondemo(request):
    return render(request,'loanamozrtiondemo.html')