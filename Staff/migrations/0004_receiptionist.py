# Generated by Django 3.1.5 on 2021-02-19 11:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HumanResource', '0007_auto_20210219_1353'),
        ('Staff', '0003_auto_20210219_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receiptionist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graduation_year', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_university_attended', models.CharField(max_length=500)),
                ('highest_education_level', models.CharField(choices=[("Bachelor's Degree", "Bachelor's Degree"), ('Masters Degree', 'Masters Degree'), ('PhD', 'PhD')], max_length=50)),
                ('schools_attended', models.CharField(max_length=500)),
                ('specialization', models.CharField(max_length=500)),
                ('places_worked', models.TextField()),
                ('shift', models.CharField(choices=[('Morning', 'Morning'), ('Evening', 'Evening'), ('Day', 'Day'), ('Night', 'Night')], max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff.department')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResource.employee')),
            ],
        ),
    ]
