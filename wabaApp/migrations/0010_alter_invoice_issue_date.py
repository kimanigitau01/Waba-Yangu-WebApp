# Generated by Django 4.2.11 on 2024-11-27 12:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wabaApp', '0009_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='issue_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
