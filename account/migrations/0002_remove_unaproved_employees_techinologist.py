# Generated by Django 4.1.3 on 2023-01-11 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unaproved_employees',
            name='Techinologist',
        ),
    ]
