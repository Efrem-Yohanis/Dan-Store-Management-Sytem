# Generated by Django 4.1.3 on 2022-12-12 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Admin', '0004_departments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentName', models.CharField(max_length=100)),
                ('departmentDescription', models.TextField(max_length=500)),
                ('departmentHead', models.CharField(max_length=40)),
            ],
        ),
    ]
