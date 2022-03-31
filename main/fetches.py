from main.models import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .models import *
import pytz
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def myfunc(e):
  return e['closing_date']

def getScholarships():

  data = requests.get(url = 'https://scholarships.gov.in/').text

  soup = BeautifulSoup(data, "html.parser")

  var = soup.find_all("div", class_="dotHead")

  schemes = []

  for i in var:
    name = i.find_next_sibling("div")
    closing_date = name.find_next_sibling("div")
    guideline = closing_date.find_next_sibling("div").find_next_sibling("div").find_next_sibling("div")
    faq = guideline.find_next_sibling("div")

    if name.get_text(strip=True)!="":
      dt = datetime.strptime(closing_date.get_text(strip=True).split()[2], '%d-%m-%Y').replace(tzinfo=pytz.UTC)

      schemes.append({"name":name.get_text(strip=True),
      "closing_date":dt,
      "guideline":'https://scholarships.gov.in'+guideline.a.attrs['href'],
      "faq":'https://scholarships.gov.in'+faq.a.attrs['href'],
      "color":"table-primary"if(closing_date.get_text(strip=True).split()[0]=="Open") else "table-danger",
      "closing_date_print":dt.strftime("%d-%b-%Y")})

  schemes=sorted(schemes, key=myfunc, reverse=True)

  return schemes

def dict_diff(a,b):
  for key in a:
    try:
      if a[key]!=b[key]:
        return 1
    except:
      pass
  return 0

def updateScholarships():
  cur = getScholarships()
  prev = list(SchemeScholarships.objects.all())

  changes = []

  for curr in cur:
    have = [i for i,x in enumerate(prev) if x.name==curr['name']]
    if len(have)==1:
      if dict_diff(prev[have[0]].__dict__,curr):
        changes.append(["edit",prev[have[0]].__dict__,curr])

        #update in db
        db = SchemeScholarships.objects.get(name=curr['name'])
        db.closing_date = curr['closing_date']
        db.guideline = curr['guideline']
        db.faq = curr['faq']
        db.save()
      del(prev[have[0]])

    else:
      changes.append(["add",curr])

      #add in db
      db = SchemeScholarships()
      db.name = curr['name']
      db.closing_date = curr['closing_date']
      db.guideline = curr['guideline']
      db.faq = curr['faq']
      db.save()
      pass

  for prevv in prev:
    changes.append(["delete",prevv.__dict__])
    
    #delete from db
    db = SchemeScholarships.objects.filter(name=prevv.name)
    db.delete()

  if len(changes)>0:
    add=[]
    edit=[]
    delete=[]
    for i in changes:
      if i[0]=='add':
        add.append(i[1])
      elif i[0]=='edit':
        edit.append(i[2])
      elif i[0]=='delete':
        delete.append(i[1])

    subject = 'Scholarships Schemes Changed'
    html_message = render_to_string('main/scheme_update.html', {'add':add, 'edit':edit, 'delete':delete})
    from_email = 'Sahayata Portal <'+settings.EMAIL_HOST_USER+'>'
    to = [i.Email for i in MailForm.objects.filter(Scholarship=True)]
    for t in to:
      send_mail(subject, '', from_email, [t], html_message=html_message)