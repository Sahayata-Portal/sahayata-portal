from django.contrib import admin
from main.models import *

# Register your models here.
class SchemeAdmin(admin.ModelAdmin):
  list_display = ['name', 'description', 'eligibility']


class MailAdmin(admin.ModelAdmin):
  list_display = ['Name', 'Email', 'Scholarship','Social','Employment']

admin.site.register(Scheme,SchemeAdmin)
admin.site.register(MailForm,MailAdmin)