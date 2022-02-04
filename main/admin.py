from django.contrib import admin
from main.models import *

# Register your models here.
class SchemeAdmin(admin.ModelAdmin):
  list_display = ['name', 'description', 'eligibility']


admin.site.register(Scheme,SchemeAdmin)