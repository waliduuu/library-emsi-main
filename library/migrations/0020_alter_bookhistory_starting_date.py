# Generated by Django 4.2.2 on 2023-09-05 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0019_rename_returned_date_bookhistory_starting_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookhistory',
            name='starting_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
