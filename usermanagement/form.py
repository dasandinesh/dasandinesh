from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from usermanagement.models import customer,receiptamount,accounts,EMItype,sourcetype,weeklyloancreate,monthlyloancreate
from django.contrib.admin.widgets import AdminDateWidget



class customerform(forms.ModelForm):
    class Meta:
        model =customer
        fields="__all__"

class EMItypeform(forms.ModelForm):
    class Meta:
        model =EMItype
        fields="__all__"

class sourcetypeform(forms.ModelForm):
    class Meta:
        model =sourcetype
        fields="__all__"

class weeklyloancreateform(forms.ModelForm):
    class Meta:
        model =weeklyloancreate
        fields="__all__"

class DateInput(forms.DateInput):
    input_type = 'date'

class monthlyloancreateform(forms.ModelForm):
    class Meta:
        model =monthlyloancreate
        fields=['monthlylan_loan_name','monthlylan_customer_name','monthlylan_EMItype','monthlylan_sourcetype','monthlylan_amount','monthlylan_agreement_peride','monthlylan_firstemidate','per_day_fine','pending_flag','total_receipt_amount','total_fine_amount','lone_type','autofinace','homeloanifo','prof','loan_phone_no']
        widgets={
            'monthlylan_firstemidate':DateInput(),
        }

class receiptamountform(forms.ModelForm):
    class Meta:
        model =receiptamount
        fields=['customer_receipter_name','receipt_emi_date','receipt_amount']
        widgets={
            'receipt_emi_date ':DateInput()
        }

