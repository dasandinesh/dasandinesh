from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class EMItype(models.Model):
    EMItype_name =models.CharField(max_length=20)
    EMI_daylength = models.IntegerField()
    EMi_amount = models.IntegerField()
    def __str__(self):
        return self.EMItype_name

class sourcetype(models.Model):
    sourcetype_name=models.CharField(max_length=25)
    source = models.CharField(max_length=15)
    source_amount=models.IntegerField()
    source_discretion = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.sourcetype_name

class customer(models.Model):
    customer_name= models.CharField(max_length=25)
    customer_dateofbirth=models.DateField(blank=True)
    customer_sex=models.CharField(max_length=10)
    customer_createdate =  models.DateField(auto_now_add=True)
    customer_phone= models.IntegerField()
    customer_community =models.CharField(max_length=20)
    customer_Doorno= models.CharField(max_length=25)
    customer_street_name= models.CharField(max_length=25)
    customer_area_name= models.CharField(max_length=25)
    customer_finance_amount=models.IntegerField()
    customer_paid_amount=models.IntegerField()
    customer_pending_amount=models.IntegerField()
    customer_acnumber =models.CharField(max_length=25)
    customer_ifsc=models.CharField(max_length=25)
    customer_bankname=models.CharField(max_length=25)
    customer_brach=models.CharField(max_length=25)
    customer_pannumber=models.CharField(max_length=15)
    customer_occupations=models.CharField(max_length=20)
    customer_idproof=models.ImageField()
    customer_photo=models.ImageField()
    pending_flag=models.IntegerField(blank=True)
    def __str__(self):
        return self.customer_name

class weeklyloancreate(models.Model):
    weeklylan_customer_name=models.CharField(max_length=25)
    weeklylan_loan_name=models.CharField(max_length=25)
    weeklylan_EMItype=models.CharField(max_length=20)
    weeklylan_sourcetype=models.CharField(max_length=20)
    weeklylan_date=models.DateField(auto_now_add=True)
    weeklylan_date_demant=models.DateField()
    weeklylan_amount=models.IntegerField()
    weeklylan_totalweek=models.IntegerField()
    weeklylan_weeklyEMI=models.IntegerField()
    per_day_fine=models.IntegerField()
    pending_flag=models.IntegerField(blank=True)
    total_receipt_amount=models.IntegerField()
    total_fine_amount=models.IntegerField()
    lone_type=models.CharField(max_length=25)
    autofinace=models.CharField(max_length=25)
    homeloanifo=models.CharField(max_length=25)
    prof=models.ImageField()
    loan_phone_no=models.IntegerField()

class monthlyloancreate(models.Model):
    monthlylan_customer_name=models.CharField(max_length=25,blank=True)
    monthlylan_loan_name=models.CharField(max_length=25,blank=True)
    monthlylan_EMItype=models.CharField(max_length=25,blank=True)
    monthlylan_sourcetype=models.CharField(max_length=25,blank=True)
    monthlylan_date=models.DateField(auto_now_add=True)
    monthlylan_amount=models.IntegerField(blank=True)
    monthlylan_agreement_peride=models.IntegerField(blank=True)
    monthlylan_firstemidate=models.DateField(blank=True)
    per_day_fine=models.IntegerField(blank=True)
    pending_flag=models.IntegerField(blank=True)
    total_receipt_amount=models.IntegerField(blank=True)
    total_fine_amount=models.IntegerField(blank=True)
    lone_type=models.CharField(max_length=25,blank=True)
    autofinace=models.CharField(max_length=25,blank=True)
    homeloanifo=models.CharField(max_length=25,blank=True)
    prof=models.ImageField(blank=True)
    loan_phone_no=models.IntegerField(blank=True)

class receiptamount(models.Model):
    customer_receipter_name=models.CharField(max_length=25)
    loan_name=models.CharField(max_length=25)
    receipt_date =  models.DateField(auto_now_add=True)
    receipt_emi_date = models.DateField(blank=True)
    receipt_amount = IntegerField()
    receipt_discretion = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.customer_receipter_name

class accounts(models.Model):
    amount_type = models.CharField(max_length=15)
    customer_name_payment= models.CharField(max_length=15)

class weeklydemand(models.Model):
    weeklydemand_loan_name=models.CharField(max_length=25)
    emi_amount=models.IntegerField()
    emi_demand_date = models.DateField(blank=True)
    pending_flag =models.IntegerField()

class updatedate(models.Model):
    last_update_date = models.DateField(blank=True)

class pendingfine(models.Model):
    fine_customer=models.CharField(max_length=25)
    fine_date=models.DateField()
    fine_amount=models.IntegerField()


    
