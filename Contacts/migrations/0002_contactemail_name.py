# Generated by Django 5.1.4 on 2025-01-06 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactemail',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
