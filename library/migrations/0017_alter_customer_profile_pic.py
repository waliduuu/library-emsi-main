# Generated by Django 4.1.5 on 2023-09-04 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profilepic.png', null=True, upload_to=''),
        ),
    ]
