# Generated by Django 3.1 on 2023-12-13 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0003_auto_20231213_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]