# Generated by Django 3.1.4 on 2021-10-18 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0006_auto_20211018_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthlyloancreate',
            name='monthlylan_totalweek',
        ),
    ]