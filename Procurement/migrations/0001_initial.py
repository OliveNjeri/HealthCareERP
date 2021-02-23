# Generated by Django 3.1.5 on 2021-02-22 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Staff', '0006_auto_20210219_1645'),
        ('Hospital', '0010_auto_20210219_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_number', models.CharField(max_length=200, unique=True)),
                ('item', models.CharField(max_length=200)),
                ('ordered_on', models.DateTimeField()),
                ('delivery_by', models.DateTimeField()),
                ('quantity', models.FloatField()),
                ('unit_price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('order_approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff.departmentdirector')),
                ('ordered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.departmentchairperson')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=200)),
                ('type_of_supply', models.CharField(max_length=500)),
                ('date_contracted', models.DateTimeField()),
                ('contract_type', models.CharField(choices=[('Permanent Supplier', 'Permanent Supplier'), ('Temporary Supplier', 'Temporary Supplier')], max_length=200)),
                ('postal_code', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff.departmentdirector')),
                ('vetted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.departmentchairperson')),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivered_on', models.DateTimeField()),
                ('quantity', models.FloatField()),
                ('unit_price', models.FloatField()),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff.departmentdirector')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Procurement.purchase')),
                ('received_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.departmentchairperson')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Procurement.supplier')),
            ],
            options={
                'verbose_name': 'Supply',
                'verbose_name_plural': 'Supplies',
            },
        ),
        migrations.AddField(
            model_name='purchase',
            name='ordered_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Procurement.supplier'),
        ),
    ]
