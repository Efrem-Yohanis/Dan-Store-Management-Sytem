# Generated by Django 4.1.3 on 2022-12-13 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0029_vendor_vendoradded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendorAdded',
            field=models.DateField(auto_now_add=True),
        ),
    ]