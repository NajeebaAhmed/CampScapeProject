# Generated by Django 3.1 on 2023-12-20 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0004_review_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]