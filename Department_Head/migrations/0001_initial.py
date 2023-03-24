# Generated by Django 4.1.3 on 2023-01-04 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Store_manager', '0067_alter_employe_request_form1_permanent_dept_head_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='dept_request_form2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('unit', models.CharField(blank=True, max_length=100, null=True)),
                ('req_qty', models.CharField(blank=True, max_length=100, null=True)),
                ('Remark', models.CharField(blank=True, max_length=100, null=True)),
                ('employe_request_form1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Store_manager.employe_request_form1')),
            ],
        ),
        migrations.CreateModel(
            name='dept_request_form1_permanent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('dept_head_Action', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=200, null=True)),
                ('Store_Keeper_Action', models.CharField(choices=[('Pending', 'Pending'), ('Allowed', 'Allowed'), ('wait', 'wait'), ('Reject', 'Reject')], default='Pending', max_length=200, null=True)),
                ('Request_by', models.CharField(blank=True, max_length=100, null=True)),
                ('Department', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('unit', models.CharField(blank=True, max_length=100, null=True)),
                ('req_qty', models.CharField(blank=True, max_length=100, null=True)),
                ('Remark', models.CharField(blank=True, max_length=100, null=True)),
                ('checkd_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Store_manager.employ')),
                ('request_store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Store_manager.allstore')),
            ],
        ),
        migrations.CreateModel(
            name='dept_request_form1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('Request_by', models.CharField(blank=True, max_length=100, null=True)),
                ('Department', models.CharField(blank=True, max_length=100, null=True)),
                ('checkd_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Store_manager.employ')),
                ('request_store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Store_manager.allstore')),
            ],
        ),
    ]
