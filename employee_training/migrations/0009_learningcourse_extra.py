# Generated by Django 5.1.5 on 2025-01-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_training', '0008_learningcourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningcourse',
            name='extra',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
