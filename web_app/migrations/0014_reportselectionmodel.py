# Generated by Django 3.2.9 on 2021-11-24 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0013_auto_20211123_0346'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportSelectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cyto', models.CharField(max_length=30)),
                ('flow', models.CharField(max_length=30)),
                ('fish', models.CharField(max_length=30)),
                ('morpho', models.CharField(max_length=30)),
                ('molecular', models.CharField(max_length=30)),
                ('fishadd', models.CharField(max_length=30)),
                ('cunsult', models.CharField(max_length=30)),
            ],
        ),
    ]