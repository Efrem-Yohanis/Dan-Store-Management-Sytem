# Generated by Django 4.1.3 on 2023-01-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0072_employ_collage_employ_document_employ_filed_study_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe_request_form1_permanent',
            name='Recival_status_by_Employer',
            field=models.CharField(choices=[('Received ', 'Received'), ('Not_Received ', 'Not_Received'), ('Returned', 'Returned')], max_length=200, null=True),
        ),
    ]
