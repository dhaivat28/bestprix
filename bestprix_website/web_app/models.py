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

class snapdeal(models.Model):
	name = models.CharField(max_length=200)
	url = models.TextField(null=False)
	price = models.IntegerField(null=False)

class amazon(models.Model):
	name = models.CharField(max_length=200)
	url = models.TextField(null=False)
	price = models.IntegerField(null=False)

class user_detail(models.Model):
	email_id = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	s_q = models.CharField(max_length=200)
	s_a = models.CharField(max_length=100)
