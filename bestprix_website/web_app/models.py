from __future__ import unicode_literals

from django.db import models

# Create your models here.
class flipkart(models.Model):
	name = models.CharField(max_length=200)
	url = models.TextField(null=False)
	price = models.IntegerField(null=False)

class infibeam(models.Model):
	name = models.CharField(max_length=200)
	url = models.TextField(null=False)
	price = models.IntegerField(null=False)
