# Generated by Django 4.1.3 on 2023-01-04 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Department_Head', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept_request_form2',
            name='employe_request_form1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Department_Head.dept_request_form1'),
        ),
    ]
