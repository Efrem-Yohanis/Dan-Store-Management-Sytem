# Generated by Django 4.1.3 on 2022-12-19 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0042_remove_employ_role_employ_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Action',
            field=models.CharField(choices=[('New_Add', 'New_Add'), ('Removed', 'Removed')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Approved',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Order_Id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Reason',
            field=models.CharField(blank=True, choices=[('Returned Material', 'Returned Material'), ('Gift', 'Gift'), ('Purchased', 'Purchased'), ('Other', 'Other')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='add_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='serial_No',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='vender',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='last_update',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
