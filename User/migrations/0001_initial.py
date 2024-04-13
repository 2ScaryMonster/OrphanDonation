# Generated by Django 5.0.1 on 2024-04-11 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0009_tbl_donationtype'),
        ('Guest', '0009_rename_farmer_tbl_feedback_orphnage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_title', models.CharField(max_length=50)),
                ('donation_description', models.CharField(max_length=50)),
                ('donation_date', models.DateField(auto_now_add=True)),
                ('amount', models.CharField(max_length=50)),
                ('donationtype_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_donationtype')),
                ('orphanage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_orphanage')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]