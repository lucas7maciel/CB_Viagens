# Generated by Django 5.0.3 on 2024-03-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('price_confort', models.CharField(max_length=15)),
                ('price_econ', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=40)),
                ('duration', models.CharField(max_length=10)),
                ('seat', models.CharField(max_length=3)),
                ('bed', models.CharField(max_length=3)),
                ('customerId', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
