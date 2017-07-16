# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-16 06:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pfirst_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('plast_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('pemail', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('mobile_ph', models.CharField(max_length=10, verbose_name='Mobile Phone')),
                ('paddress', models.TextField(verbose_name='Address')),
                ('job', models.CharField(max_length=50, verbose_name='Job')),
                ('office_addr', models.TextField(verbose_name='Office Address')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(verbose_name='Address')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('mobile_ph', models.CharField(blank=True, max_length=10, null=True, verbose_name='Mobile Phone')),
                ('doj', models.DateField(verbose_name='Date of Joining')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Parent')),
            ],
        ),
    ]
