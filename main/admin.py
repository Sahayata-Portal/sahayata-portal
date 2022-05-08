from django.contrib import admin
from main.models import *

# Register your models here.
class SchemeAdmin(admin.ModelAdmin):
  list_display = ['name', 'description', 'eligibility']


class MailAdmin(admin.ModelAdmin):
  list_display = ['UUID','Name', 'Email', 'Scholarship','Social','Employment']

admin.site.register(Scheme,SchemeAdmin)
admin.site.register(MailForm,MailAdmin)

class SchemeScholarshipsAdmin(admin.ModelAdmin):
  list_display = ['id','name','closing_date','guideline','faq']

admin.site.register(SchemeScholarships,SchemeScholarshipsAdmin)

class TranslationsAdmin(admin.ModelAdmin):
  list_display = ['id','text','lang',"tran"]

admin.site.register(Translations,TranslationsAdmin)