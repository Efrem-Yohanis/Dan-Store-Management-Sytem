# Generated by Django 4.1.3 on 2023-01-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0075_itemhistory_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemhistory',
            name='gift_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]