# Generated by Django 3.1.4 on 2021-10-20 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0007_remove_monthlyloancreate_monthlylan_totalweek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyloancreate',
            name='autofinace',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='monthlyloancreate',
            name='homeloanifo',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='monthlyloancreate',
            name='loan_phone_no',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='monthlyloancreate',
            name='lone_type',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='monthlyloancreate',
            name='monthlylan_EMItype',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='monthlyloancreate',
            name='monthlylan_agreement_peride',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='monthlyloancreate',
            name='monthlylan_amount',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='monthlyloancreate',
            name='monthlylan_customer_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='monthlyloancreate',
            name='monthlylan_loan_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='monthlyloancreate',
            name='monthlylan_sourcetype',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='monthlyloancreate',
            name='per_day_fine',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='monthlyloancreate',
            name='prof',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='monthlyloancreate',
            name='total_fine_amount',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='monthlyloancreate',
            name='total_receipt_amount',
            field=models.IntegerField(blank=True),
        ),
    ]
