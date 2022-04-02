from django.shortcuts import render, HttpResponse
from main.models import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json
from urllib.parse import quote
import os
import ssl,urllib
from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from main.fetches import *
import random
from django.template.loader import render_to_string

# Create your views here.
def HomePage(request):
  MSG=''
  return render(request,"main/home.html",{'msg':MSG})


def SchemePage(request):

  schemes = Scheme.objects.all()


  
  return render(request,"main/schemes.html",{"schemes":schemes})

def Ourteam(request):

  
  return render(request,"main/ourteam.html")


def Scholarships(request):

  schemes = getScholarships()

  return render(request,"main/scholarships.html",{"data":schemes})

def about(request):

  
  return render(request,"main/about.html")

def Employment(request):
  context = ssl._create_unverified_context()
  data = urllib.request.urlopen("https://eshram.gov.in/employment-schemes", context=context).read()

  soup = BeautifulSoup(data, "html.parser")

  var = soup.find_all("div", class_="schemes-text")

  schemes = []

  for i in var:
    schemes.append(str(i))
  return render(request,"main/Employment.html",{"data":schemes})

def social(request):
  context = ssl._create_unverified_context()
  data = urllib.request.urlopen("https://eshram.gov.in/social-security-welfare-schemes", context=context).read()

  soup = BeautifulSoup(data, "html.parser")

  var = soup.find_all("div", class_="schemes-text")

  schemes = []

  for i in var:
    schemes.append(str(i))
  return render(request,"main/social.html",{"data":schemes})

@csrf_exempt
def TextToVoice(request):
  text = json.loads(request.body).get("text")

  soup = BeautifulSoup(text, "html.parser")
  text = soup.get_text()
  text = quote(text)

  url = "https://voicerss-text-to-speech.p.rapidapi.com/"
  querystring = {"key":os.environ.get("TEXT_TO_SPEECH_KEY")}

  payload = "src="+text
  payload = payload + "&hl=en-us&v=Mary&r=0&c=mp3&f=44khz_16bit_stereo"

  headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "voicerss-text-to-speech.p.rapidapi.com",
    'x-rapidapi-key': os.environ.get('X_RAPIDAPI_KEY')
  }

  response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

  voice = response

  return HttpResponse(voice, content_type='audio/mp3')

def subscribe(request):
  MSG=''
  Type=1
  form = EmailForm()
  if request.method == 'POST':
    if request.POST.get('type')=='1':
      email = request.POST.get("Email")
      if len(MailForm.objects.filter(Email=email))==0:
        MailForm(Email=request.POST.get("Email"),  Name="").save()
      cur = MailForm.objects.filter(Email=email)[0]
      cur.OTP = str(random.randint(100000, 999999))
      cur.Tries = 0
      cur.save()
      mail = render_to_string('main/otp.html', {'otp':str(cur.OTP)})
      send_mail('OTP for Sahayata Portal verification','','Sahayata Portal <'+settings.EMAIL_HOST_USER+'>',[email],html_message=mail)
      MSG = 'OTP sent to '+email
      form = OTPForm({'email':email})
      Type=2

    elif request.POST.get('type')=='2':
      email=request.POST.get("email")
      otp=request.POST.get("OTP")
      try:
        temp = MailForm.objects.get(Email=email)
        if otp == temp.OTP:
          form = SubsForm(instance=temp)
          Type = 3
        else:
          tries = temp.Tries
          if tries==2:
            MSG = 'Incorrect OTP entered 3 times !'
          else:
            MSG = 'Incorrect OTP ! ' + str(2-tries) + ' tries left'
            MailForm.objects.filter(Email=email).update(Tries=tries+1)
            form = OTPForm({'email':request.POST.get("email")})
            Type=2
      except:
        pass
      
    elif request.POST.get('type')=='3':
      email=request.POST.get("Email")
      otp=request.POST.get("OTP")
      temp = MailForm.objects.filter(Email=email).filter(OTP=otp)
      if len(temp)>0:
        temp=temp[0]
        thisform = SubsForm(request.POST, instance=temp)
        if thisform.is_valid():
          thisform.save()
          MailForm.objects.filter(Email=email).filter(OTP=otp).update(Active=True)
        MSG = 'Data updated'
      else:
        MSG = 'Error updating data, please try again'

    else:
      MSG='Invalid form submission !'

  return render(request, 'main/subscribe.html', {'form':form, 'msg':MSG, 'type':Type, 'form_head':'Subscribe to email notifications'})

def Unsubscribe(request, uuid):
  obj = []
  try:
    obj = MailForm.objects.filter(UUID=uuid)
  except:
    pass
  if len(obj)==0:
    return render(request,"main/unsubscribe.html",{"msg":'You are already unsubscribed'})
  if request.method == 'POST':
    obj.delete()
    return render(request,"main/unsubscribe.html",{"msg":'You are successfully unsubscribed'})
  
  return render(request,"main/unsubscribe.html",{"ask":1})

def Update(request, schemetype):
  if schemetype=="scholarship":
    updateScholarships()

  return HttpResponse("OK")

  # Create your views here.
def Women(request):
  context = ssl._create_unverified_context()
  data = urllib.request.urlopen("https://wcd.nic.in/schemes-listing/2405", context=context).read()

  soup = BeautifulSoup(data, "html.parser")

  var = soup.find_all("div", class_="item-list")[0].find_all("span",class_="field-content")
  
  schemes = []

  for i in var:
    name=i.find_all("a")[0]
    schemes.append([name.get_text(strip=True),'https://wcd.nic.in'+name.attrs['href']])
  return render(request,"main/Women.html",{"data":schemes})
