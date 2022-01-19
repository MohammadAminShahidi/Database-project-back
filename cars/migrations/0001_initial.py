# Generated by Django 3.2.10 on 2022-01-18 17:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PID', models.CharField(max_length=8, unique=True)),
                ('Type', models.CharField(max_length=10)),
                ('Model', models.CharField(max_length=20)),
                ('Tip', models.CharField(max_length=10)),
                ('ProductionDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('Capacity', models.IntegerField()),
                ('Fuel', models.CharField(max_length=20)),
                ('Color', models.CharField(max_length=30)),
                ('Room', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Car_motor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CMID', models.IntegerField(unique=True)),
                ('CarID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
            options={
                'unique_together': {('CMID', 'CarID')},
            },
        ),
        migrations.CreateModel(
            name='Car_chassis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CCID', models.IntegerField(unique=True)),
                ('CarID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
            options={
                'unique_together': {('CCID', 'CarID')},
            },
        ),
    ]
