# Generated by Django 3.1 on 2023-12-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Packages', '0004_auto_20231210_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='product_description',
            field=models.TextField(null=True),
        ),
    ]
