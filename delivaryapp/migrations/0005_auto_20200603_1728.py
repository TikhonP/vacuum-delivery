# Generated by Django 3.0.6 on 2020-06-03 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivaryapp', '0004_auto_20200127_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userplaces',
            name='id',
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='wuser',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='userplaces',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userplaces',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='userplaces',
            name='place',
            field=models.CharField(default=0, max_length=3),
        ),
    ]
