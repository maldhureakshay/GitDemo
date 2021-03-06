# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-16 08:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_number', models.CharField(max_length=30)),
                ('flat_created', models.DateTimeField(auto_now_add=True)),
                ('flat_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('society_name', models.CharField(max_length=50)),
                ('society_address', models.CharField(max_length=30)),
                ('society_city', models.CharField(max_length=30)),
                ('society_state', models.CharField(max_length=30)),
                ('society_country', models.CharField(max_length=30)),
                ('society_zipcode', models.CharField(max_length=10)),
                ('society_created', models.DateTimeField(auto_now_add=True)),
                ('society_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('Security', 'Security'), ('Manager', 'Manager'), ('Owner', 'Owner')], default='Owner', max_length=5)),
                ('user_firstname', models.CharField(max_length=30)),
                ('user_lastname', models.CharField(max_length=30)),
                ('user_email', models.CharField(max_length=50)),
                ('user_phone', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('user_address', models.CharField(max_length=30)),
                ('user_city', models.CharField(max_length=30)),
                ('user_state', models.CharField(max_length=30)),
                ('user_country', models.CharField(max_length=30)),
                ('user_zipcode', models.CharField(max_length=10)),
                ('user_created', models.DateTimeField(auto_now_add=True)),
                ('user_updated', models.DateTimeField(auto_now=True)),
                ('flat', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='wing', chained_model_field='wing', on_delete=django.db.models.deletion.CASCADE, to='societyapp.Flat')),
                ('society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='societyapp.Society')),
            ],
        ),
        migrations.CreateModel(
            name='Wing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wing_name', models.CharField(max_length=30)),
                ('wing_created', models.DateTimeField(auto_now_add=True)),
                ('wing_updated', models.DateTimeField(auto_now=True)),
                ('society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='societyapp.Society')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='wing',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='society', chained_model_field='society', on_delete=django.db.models.deletion.CASCADE, to='societyapp.Wing'),
        ),
        migrations.AddField(
            model_name='flat',
            name='society',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='societyapp.Society'),
        ),
        migrations.AddField(
            model_name='flat',
            name='wing',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='society', chained_model_field='society', on_delete=django.db.models.deletion.CASCADE, to='societyapp.Wing'),
        ),
        migrations.AlterUniqueTogether(
            name='wing',
            unique_together=set([('society', 'wing_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='flat',
            unique_together=set([('wing', 'flat_number')]),
        ),
    ]
