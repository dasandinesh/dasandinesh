from django import forms
from django.db import models
from django.db.models import fields
from notification.models import officenotifications,customernotiications
from django.contrib.admin.widgets import AdminDateWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class officenotificationsform(forms.ModelForm):
    class Meta:
        model =officenotifications
        fields=['name', 'date', 'description','amount']
        widgets = {
            'date': DateInput(),
        }

class customernotiicationsform(forms.ModelForm):
    class Meta:
        model =customernotiications
        fields=['name', 'date', 'description','amount']
        widgets = {
            'date': DateInput(),
        }

class DateInput(forms.DateInput):
    input_type = 'date'

