# Generated by Django 4.2.2 on 2023-09-04 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookreturning',
            old_name='date_fin_emprunt',
            new_name='return_date',
        ),
        migrations.RemoveField(
            model_name='bookreturning',
            name='transaction_id',
        ),
        migrations.DeleteModel(
            name='confirmationAdress',
        ),
    ]