# Generated by Django 3.0.1 on 2020-01-27 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivaryapp', '0003_orders_wuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='wuser',
            field=models.CharField(max_length=20),
        ),
    ]
