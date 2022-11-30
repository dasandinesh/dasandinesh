from django.shortcuts import render,redirect
from notification.models import officenotifications,customernotiications
from notification.form import officenotificationsform, customernotiicationsform

# Create your views here.
def customernotification(request):
    if request.method =="POST":
        form = customernotiicationsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customernotiications')
    else:
        obj=customernotiications.objects.all()
        context={
            'form':customernotiicationsform,
            'obj':obj
        }
        return render(request,'customernotifigation.html',context)
    return render(request,'customernotifigation.html')

def officenotifigation(request):
    if request.method =="POST":
        form = officenotificationsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/officenotifigation')
    else:
        obj=officenotifications.objects.all()
        context={
            'form':officenotificationsform,
            'obj':obj
        }
        return render(request,'officenotifigation.html',context)
    return render(request,'officenotifigation.html')