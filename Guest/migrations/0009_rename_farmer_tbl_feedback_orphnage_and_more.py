# Generated by Django 5.0.2 on 2024-04-09 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0008_tbl_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_feedback',
            old_name='farmer',
            new_name='orphnage',
        ),
        migrations.RenameField(
            model_name='tbl_feedback',
            old_name='market',
            new_name='user',
        ),
    ]