# Generated by Django 3.2.9 on 2021-11-22 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_rename_inputmodel_accessionmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccessionModel',
            new_name='PatientModel',
        ),
    ]
