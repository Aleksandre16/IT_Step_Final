# Generated by Django 5.1.7 on 2025-03-25 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
