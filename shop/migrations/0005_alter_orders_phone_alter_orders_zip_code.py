# Generated by Django 4.2.1 on 2023-09-19 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.IntegerField(default=0),
        ),
    ]
