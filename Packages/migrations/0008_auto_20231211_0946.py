# Generated by Django 3.1 on 2023-12-11 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Packages', '0007_auto_20231210_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='package',
            name='start_date',
        ),
    ]