# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class ques_ans(models.Model):
    username = models.CharField(max_length=10)
    ques_id = models.CharField(max_length=3)
    ques = models.CharField(max_length=100)
    ans = models.CharField(null = True,max_length=100)

class images(models.Model):
    username = models.CharField(max_length=10,primary_key = True)
    profile = models.ImageField(null = True)
    image1 = models.ImageField(null = True)
    image2 = models.ImageField(null = True)
    image3 = models.ImageField(null = True)
    image4 = models.ImageField(null = True)
