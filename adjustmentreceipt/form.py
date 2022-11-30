from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from adjustmentreceipt.models import creditadjustmentreceipt,deiptadjustmentreceipt,fineadjustment
from django.contrib.admin.widgets import AdminDateWidget


class DateInput(forms.DateInput):
    input_type = 'date'

class creditadjustmentreceiptform(forms.ModelForm):
    class Meta:
        model =creditadjustmentreceipt
        fields=['loan_name','receipt_date','adjustment_credit_amount','reason']
        widgets={
            'receipt_date':DateInput(),
        }

class deiptadjustmentreceiptform(forms.ModelForm):
    class Meta:
        model =deiptadjustmentreceipt
        fields=['loan_name','date','adjustment_deipt_amount','reason']
        widgets={
            'date':DateInput(),
        }

class fineadjustmentform(forms.ModelForm):
    class Meta:
        model =fineadjustment
        fields=['loan_name','fine_date','fine_amout','reason']
        widgets={
            'fine_date':DateInput(),
        }