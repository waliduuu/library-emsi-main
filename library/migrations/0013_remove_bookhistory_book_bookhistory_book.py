# Generated by Django 4.1.5 on 2023-09-04 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_bookhistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookhistory',
            name='book',
        ),
        migrations.AddField(
            model_name='bookhistory',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.book'),
        ),
    ]
