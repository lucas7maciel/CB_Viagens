# Generated by Django 5.0.3 on 2024-04-17 12:49

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('price_confort', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_econ', models.DecimalField(decimal_places=2, max_digits=10)),
                ('city', models.CharField(max_length=40)),
                ('date', models.DateField(default=datetime.date.today)),
                ('duration', models.CharField(max_length=10)),
                ('seat', models.CharField(max_length=3)),
                ('bed', models.CharField(max_length=3)),
                ('customer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
