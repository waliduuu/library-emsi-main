# Generated by Django 4.1.5 on 2023-08-27 19:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_emprunt_transaction_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empruntitem',
            name='date_debut_emprunt',
        ),
        migrations.AddField(
            model_name='emprunt',
            name='date_emprunt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empruntitem',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='bookreturning',
            name='date_fin_emprunt',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='confirmationAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=30, null=True)),
                ('addressl2', models.CharField(max_length=30, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('state', models.CharField(max_length=30, null=True)),
                ('zipcode', models.CharField(max_length=30, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.customer')),
                ('emprunt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.emprunt')),
            ],
        ),
    ]
