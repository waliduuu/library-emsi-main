# Generated by Django 4.1.5 on 2023-08-27 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_remove_empruntitem_date_debut_emprunt_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprunt',
            name='date_emprunt',
        ),
    ]