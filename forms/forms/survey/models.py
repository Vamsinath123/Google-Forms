from django.db import models

class data(models.Model):
	username1 = models.CharField(max_length=150)
	ans1 = models.CharField(max_length=200)
	ans2 = models.CharField(max_length=200)
	ans3 = models.CharField(max_length=200)
# Create your models here.
