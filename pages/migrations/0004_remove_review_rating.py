# Generated by Django 3.2.18 on 2023-05-07 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]
