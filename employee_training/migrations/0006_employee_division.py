# Generated by Django 5.1.5 on 2025-01-21 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_training', '0005_employee_reg_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='division',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee_training.division'),
            preserve_default=False,
        ),
    ]
