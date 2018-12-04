# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime
from django.core.validators import RegexValidator
from smart_selects.db_fields import ChainedForeignKey 
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

USER_TYPES = (
        ('Security', 'Security'),
        ('Manager', 'Manager'),
        ('Owner', 'Owner'),
    )


class Society(models.Model):
    society_name    = models.CharField(max_length = 50)
    society_address = models.CharField(max_length = 30)
    society_city    = models.CharField(max_length = 30)
    society_state   = models.CharField(max_length = 30)
    society_country = models.CharField(max_length = 30)
    society_zipcode = models.CharField(max_length = 10)
    society_created = models.DateTimeField(auto_now_add=True)
    society_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.society_name

class Wing(models.Model):
    society         = models.ForeignKey(Society, on_delete= models.CASCADE)
    wing_name       = models.CharField(max_length = 30)
    wing_created    = models.DateTimeField(auto_now_add=True)
    wing_updated    = models.DateTimeField(auto_now=True)
    def __str__(self):
        return  self.society.society_name+' Wing-'+self.wing_name
    class Meta:
        unique_together = ('society', 'wing_name',)


class Flat(models.Model):
    society         = models.ForeignKey(Society)
    wing            = ChainedForeignKey(
        Wing,
        chained_field="society",
        chained_model_field="society",
        show_all=False,
        auto_choose=True,
        sort=True)
    flat_number     = models.CharField(max_length = 30)
    flat_created    = models.DateTimeField(auto_now_add=True)
    flat_updated    = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'Wing-'+self.wing.wing_name+' '+self.flat_number

    class Meta:
        managed     = True
        unique_together = ('wing', 'flat_number',)


class User(models.Model):
    user_type = models.CharField(max_length=5, choices=USER_TYPES, default='Owner')
    society         = models.ForeignKey(Society)
    wing            = ChainedForeignKey(
        Wing,
        chained_field="society",
        chained_model_field="society",
        show_all=False,
        auto_choose=True,
        sort=True)
    flat            = ChainedForeignKey(
        Flat,
        chained_field="wing",
        chained_model_field="wing",
        show_all=False,
        auto_choose=True,
        sort=True)
    user_firstname  = models.CharField(max_length = 30)
    user_lastname   = models.CharField(max_length = 30)  
    user_email      = models.CharField(max_length = 50)
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    user_phone      = models.CharField(validators=[phone_regex], max_length=17)
    user_address    = models.CharField(max_length = 30)
    user_city       = models.CharField(max_length = 30)
    user_state      = models.CharField(max_length = 30)
    user_country    = models.CharField(max_length = 30)
    user_zipcode    = models.CharField(max_length = 10)
    user_created = models.DateTimeField(auto_now_add=True)
    user_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user_firstname+' '+self.user_lastname




