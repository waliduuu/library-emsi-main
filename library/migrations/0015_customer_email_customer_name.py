# Generated by Django 4.1.5 on 2023-09-04 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_remove_customer_email_remove_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
