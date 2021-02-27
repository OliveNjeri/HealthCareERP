# Generated by Django 3.1.5 on 2021-02-24 22:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HumanResource', '0016_employee_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='graduation_year',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='highest_education_level',
            field=models.CharField(blank=True, choices=[("Bachelor's Degree", "Bachelor's Degree"), ('Masters Degree', 'Masters Degree'), ('PhD', 'PhD')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_university_attended',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='places_worked',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='schools_attended',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='specialization',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]