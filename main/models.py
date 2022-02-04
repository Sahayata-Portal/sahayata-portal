from django.db import models

# Create your models here.
class Scheme(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  eligibility = models.CharField(max_length=200)