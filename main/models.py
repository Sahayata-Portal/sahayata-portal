from django.db import models

# Create your models here.
class Scheme(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  eligibility = models.CharField(max_length=200)

class MailForm(models.Model):
  # fields of the model
  Name = models.CharField(max_length = 200)
  Email = models.EmailField(max_length = 200)
  Scholarship = models.BooleanField()
  Social = models.BooleanField()

