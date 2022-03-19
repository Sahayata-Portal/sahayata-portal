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


# Create your views here.
def HomePage(request):


  return render(request,"main/home.html")


def Page2(request):

  a = ["Yash","Riya","Priyasha","Priyanka"]
  b = ["abc","def"]


  
  return render(request,"main/page2.html",{"names":a,"det":b})


def SchemePage(request):

  schemes = Scheme.objects.all()


  
  return render(request,"main/schemes.html",{"schemes":schemes})

def Ourteam(request):

  
  return render(request,"main/ourteam.html")

def myfunc(e):
  e[1]
  dt = datetime.strptime(e[1], '%d-%m-%Y')
  return dt

def Scholarships(request):

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
      schemes.append([name.get_text(strip=True),
      closing_date.get_text(strip=True).split()[2],
      'https://scholarships.gov.in'+guideline.a.attrs['href'],
      'https://scholarships.gov.in'+faq.a.attrs['href']
      ,"table-primary"if(closing_date.get_text(strip=True).split()[0]=="Open") else "table-danger"])

  schemes=sorted(schemes, key=myfunc, reverse=True)

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

@csrf_exempt
def TextToVoice(request):
  text = json.loads(request.body).get("text")

  soup = BeautifulSoup(text, "html.parser")
  text = soup.get_text()
  text = quote(text)

  url = "https://voicerss-text-to-speech.p.rapidapi.com/"
  querystring = {"key":os.environ.get("TEXT_TO_SPEECH_KEY")}

  payload = "src="+text
  payload = payload + "&hl=en-us&v=Mary&r=3&c=mp3&f=44khz_16bit_stereo"

  headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "voicerss-text-to-speech.p.rapidapi.com",
    'x-rapidapi-key': os.environ.get('X_RAPIDAPI_KEY')
  }

  response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

  voice = response

  return HttpResponse(voice, content_type='audio/mp3')