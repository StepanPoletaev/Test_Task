# Generated by Django 4.2.3 on 2023-07-19 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.department'),
        ),
    ]
