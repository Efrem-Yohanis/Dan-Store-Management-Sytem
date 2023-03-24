# Generated by Django 4.1.3 on 2023-01-12 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_unaproved_employees_techinologist'),
    ]

    operations = [
        migrations.CreateModel(
            name='form1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Last_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Emila', models.CharField(blank=True, max_length=200, null=True)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone1', models.CharField(max_length=200, null=True)),
                ('phone2', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='Profile/')),
                ('Titel', models.CharField(blank=True, max_length=20, null=True)),
                ('Filed_Study', models.CharField(blank=True, max_length=20, null=True)),
                ('Collage', models.CharField(blank=True, max_length=20, null=True)),
                ('grade', models.CharField(blank=True, max_length=20, null=True)),
                ('Year_Graguation', models.DateField(blank=True, null=True)),
                ('Document', models.FileField(blank=True, null=True, upload_to='File/Document')),
            ],
        ),
        migrations.CreateModel(
            name='form3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Last_Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Emila', models.CharField(blank=True, max_length=200, null=True)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone1', models.CharField(max_length=200, null=True)),
                ('phone2', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='Profile/')),
                ('Titel', models.CharField(blank=True, max_length=20, null=True)),
                ('Filed_Study', models.CharField(blank=True, max_length=20, null=True)),
                ('Collage', models.CharField(blank=True, max_length=20, null=True)),
                ('grade', models.CharField(blank=True, max_length=20, null=True)),
                ('Year_Graguation', models.DateField(blank=True, null=True)),
                ('Document', models.FileField(blank=True, null=True, upload_to='File/Document')),
                ('Branch', models.CharField(blank=True, max_length=20, null=True)),
                ('Department', models.CharField(blank=True, max_length=20, null=True)),
                ('role', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
