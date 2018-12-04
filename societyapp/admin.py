# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib import admin
from .models import Society,Wing,Flat,User



# Register your models here.
admin.site.register(Society)
admin.site.register(Wing)
admin.site.register(Flat)
admin.site.register(User)





