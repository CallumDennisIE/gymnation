# Generated by Django 3.2.18 on 2023-05-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20230512_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='capacity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
