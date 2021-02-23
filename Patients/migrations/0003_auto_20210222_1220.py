# Generated by Django 3.1.5 on 2021-02-22 09:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HumanResource', '0012_auto_20210219_1847'),
        ('Patients', '0002_auto_20210222_1203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='visit_time',
            new_name='date_recorded',
        ),
        migrations.CreateModel(
            name='PatientVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('visit_reason', models.TextField(default='Medical Checkup')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patients.patient')),
                ('recorded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HumanResource.receiptionist')),
            ],
        ),
        migrations.CreateModel(
            name='PatientComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_on_service', models.TextField(help_text='what do you think about our services as a patient? ')),
                ('recommend_us_to_others', models.TextField(help_text='Would you recommend us to other people? ')),
                ('recommedations', models.TextField(help_text='What would you like us to improve on? ')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patients.patient')),
            ],
            options={
                'verbose_name': 'Patient Comment',
            },
        ),
    ]
