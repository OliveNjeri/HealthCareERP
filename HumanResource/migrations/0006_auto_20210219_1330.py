# Generated by Django 3.1.5 on 2021-02-19 10:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HumanResource', '0005_employeecheckout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='check_out_time',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='check_in_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
