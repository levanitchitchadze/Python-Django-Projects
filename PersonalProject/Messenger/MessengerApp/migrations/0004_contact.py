# Generated by Django 4.1.3 on 2023-02-04 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessengerApp', '0003_customers_delete_newcustomers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Message', models.TextField()),
            ],
        ),
    ]
