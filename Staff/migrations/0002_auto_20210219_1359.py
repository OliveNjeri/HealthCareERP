# Generated by Django 3.1.5 on 2021-02-19 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='director',
            options={'verbose_name': 'Department Director'},
        ),
        migrations.RemoveField(
            model_name='department',
            name='director',
        ),
        migrations.AddField(
            model_name='director',
            name='department',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Staff.department'),
        ),
        migrations.AlterField(
            model_name='director',
            name='graduation_year',
            field=models.DateTimeField(default=2021),
        ),
    ]
