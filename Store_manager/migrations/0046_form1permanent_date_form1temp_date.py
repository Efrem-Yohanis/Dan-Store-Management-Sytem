# Generated by Django 4.1.3 on 2022-12-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0045_item_store_alter_itemhistory_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='form1permanent',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='form1temp',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]