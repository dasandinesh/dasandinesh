from django.db import models
from django.utils import translation

# Create your models here.
class creditadjustmentreceipt(models.Model):
    loan_name=models.CharField(max_length=25)
    receipt_date=models.DateField()
    date=models.DateField(auto_now=True)
    adjustment_credit_amount=models.CharField(max_length=25)
    reason =models.CharField(max_length=25)

class deiptadjustmentreceipt(models.Model):
    loan_name=models.CharField(max_length=25)
    receipt_date=models.DateField(auto_now=True)
    date=models.DateField()
    adjustment_deipt_amount=models.CharField(max_length=25)
    reason =models.CharField(max_length=25)

class fineadjustment(models.Model):
    loan_name=models.CharField(max_length=25)
    date=models.DateField(auto_now=True)
    fine_date=models.DateField()
    fine_amout=models.DateField(max_length=10)
    reason=models.CharField(max_length=25)
