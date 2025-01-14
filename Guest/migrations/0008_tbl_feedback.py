# Generated by Django 5.0.2 on 2024-04-09 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0007_alter_tbl_chat_orphnage_from_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_con', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
                ('farmer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_orphanage')),
                ('market', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_user')),
            ],
        ),
    ]
