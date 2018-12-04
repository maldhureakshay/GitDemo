# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core import serializers

def subcategory(request, category_id):
    return HttpResponse(serializers.serialize('json', SubCategory.objects.filter(category=category_id), fields=('pk','name')))
