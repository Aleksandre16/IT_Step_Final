# Generated by Django 5.1.7 on 2025-03-26 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rent'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='favorite_cars',
            field=models.ManyToManyField(blank=True, related_name='favorited_by', to='core.car'),
        ),
    ]
