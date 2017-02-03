from __future__ import unicode_literals

from django.db import models

# Create your models here.
class flipkart(models.Model):
	p_name = models.CharField(max_length=200)
	p_url = models.TextField()
