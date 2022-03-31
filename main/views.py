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
from .forms import SubsForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from main.fetches import *

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
  if request.method == 'POST':
    form=SubsForm(request.POST)
    if form.is_valid():
      form.save()
      MSG='Form submitted successfully !'
      return render(request, 'main/subscribe.html', {'form':SubsForm(), 'msg':MSG})
    else:
      MSG='Invalid form submission !'
      return render(request, 'main/subscribe.html', {'form':SubsForm(), 'msg':MSG})
  else:
    return render(request, 'main/subscribe.html', {'form':SubsForm(), 'msg':MSG})

def Update(request, schemetype):
  if schemetype=="scholarship":
    updateScholarships()

  return HttpResponse("OK")