# Generated by Django 4.1.3 on 2022-12-07 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store_manager', '0020_employ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatbot',
            name='me_with',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Store_manager.employ'),
        ),
    ]