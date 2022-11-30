from django.db import models

# Create your models here.class officenotifications(models.Model):
class officenotifications(models.Model):
    name=models.CharField(max_length=15)
    date=models.DateField()
    description=models.CharField(max_length=25)
    amount=models.CharField(max_length=20)

class customernotiications(models.Model):
    name=models.CharField(max_length=15)
    date=models.DateField()
    description=models.CharField(max_length=25)
    amount=models.CharField(max_length=20)
