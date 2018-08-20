# Generated by Django 2.1 on 2018-08-20 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=17, unique=True)),
                ('year', models.IntegerField()),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('dimensions', models.CharField(max_length=100)),
                ('weight', models.FloatField(default=0)),
            ],
        ),
    ]