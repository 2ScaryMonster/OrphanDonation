# Generated by Django 5.0.2 on 2024-02-23 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0009_tbl_donationtype'),
        ('Guest', '0005_tbl_orphanage_orphanage_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_title', models.CharField(max_length=50)),
                ('request_description', models.CharField(max_length=50)),
                ('request_date', models.DateField(auto_now_add=True)),
                ('request_count', models.IntegerField(default='0', null=True)),
                ('payment_amount', models.CharField(max_length=50)),
                ('donationtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_donationtype')),
                ('orphanage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_orphanage')),
            ],
        ),
    ]
