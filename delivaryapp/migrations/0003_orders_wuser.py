# Generated by Django 3.0.1 on 2020-01-27 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivaryapp', '0002_auto_20200125_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='wuser',
            field=models.CharField(default=None, max_length=20),
        ),
    ]