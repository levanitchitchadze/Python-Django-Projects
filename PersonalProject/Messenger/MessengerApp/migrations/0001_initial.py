# Generated by Django 4.1.3 on 2023-01-10 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('MobileNumber', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('BirthDate', models.DateField(verbose_name='BirthDate')),
                ('CreateDate', models.DateField(default=datetime.date.today, verbose_name='CreateDate')),
                ('Gender', models.CharField(max_length=255)),
            ],
        ),
    ]
