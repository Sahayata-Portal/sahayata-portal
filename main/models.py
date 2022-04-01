from django.db import models

# Create your models here.
class Scheme(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  eligibility = models.CharField(max_length=200)

class MailForm(models.Model):
  # fields of the model
  Name = models.CharField(max_length = 200, default=" ")
  Email = models.EmailField(max_length = 200)
  Active = models.BooleanField(default=False)
  OTP = models.CharField(max_length=6)
  Scholarship = models.BooleanField(default=False)
  Social = models.BooleanField(default=False)
  Employment = models.BooleanField(default=False)
  Tries = models.IntegerField(default=0)

class SchemeScholarships(models.Model):
  name = models.CharField(max_length=1000)
  closing_date = models.DateTimeField()
  guideline = models.URLField()
  faq = models.URLField()
  class Meta:
    verbose_name = "Scheme - Scholarship"
    verbose_name_plural = "Scheme - Scholarships"