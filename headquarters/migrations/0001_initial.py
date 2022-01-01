# Generated by Django 3.2.10 on 2022-01-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Headquarters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HqID', models.IntegerField(default=0, unique=True)),
                ('Name', models.CharField(blank=True, default='No Name', max_length=100)),
                ('Address', models.CharField(blank=True, default='No Address', max_length=500)),
            ],
        ),
    ]