# Generated by Django 4.1.3 on 2023-01-31 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0079_employe_request_form1_permanent_serial_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemhistory',
            name='taken_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]