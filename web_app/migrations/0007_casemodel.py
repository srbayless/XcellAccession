# Generated by Django 3.2.9 on 2021-11-22 18:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0006_auto_20211122_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_received', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
