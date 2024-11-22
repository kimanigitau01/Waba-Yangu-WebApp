# Generated by Django 4.2.11 on 2024-11-23 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wabaApp', '0003_rename_contact_contactmessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewCustomer',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
