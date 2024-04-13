# Generated by Django 5.0.2 on 2024-02-23 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_tbl_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_orphanage',
            name='orphanage_address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tbl_orphanage',
            name='orphanage_count',
            field=models.IntegerField(default='0', null=True),
        ),
    ]
