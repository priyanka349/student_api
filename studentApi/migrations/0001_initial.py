# Generated by Django 2.2.3 on 2021-09-02 10:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type_of_institute', models.CharField(choices=[('h', 'High School'), ('c', 'College')], max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll_number', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('f', 'female'), ('m', 'male'), ('u', 'Undisclosed')], max_length=1, null=True)),
                ('percentage', models.FloatField()),
                ('age', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(5)])),
                ('institute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studentApi.Institute')),
            ],
        ),
    ]