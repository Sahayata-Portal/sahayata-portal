import requests
import json
import os
from main.models import Translations
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
from urllib.parse import quote
from django.shortcuts import HttpResponse
from main.fetches import *

def Translate(data, lan='en'):

  if lan=='en':
    return data

  temp = Translations.objects.filter(text=data).filter(lang=lan)
  if len(temp)!=0:
    return temp[0].tran

  url = "https://cheap-translate.p.rapidapi.com/translate"

  payload = json.dumps({
      "fromLang": "auto-detect",
      "text": data,
      "to": lan
  })
  headers = {
      'content-type': "application/json",
      'x-rapidapi-host': "cheap-translate.p.rapidapi.com",
      'x-rapidapi-key': os.environ.get('X_RAPIDAPI_KEY')
      }

  response = requests.request("POST", url, data=payload, headers=headers)
  try:
    translated = json.loads(response.text)['translatedText']

    obj = Translations(text=data, lang=lan, tran=translated)
    obj.save()

    return translated
  
  except:
    return data

def TranslateList(data, lan='en'):
  text = ''
  for i in data:
    text = text + i + "       \n       "

  translated = Translate(text, lan)

  translated = translated.split("\n")[:-1]
  for i in range(len(translated)):
    translated[i].strip()

  return translated

def Voice(data, lan='en'):
  url = "https://voicerss-text-to-speech.p.rapidapi.com/"
  querystring = {"key":os.environ.get("TEXT_TO_SPEECH_KEY")}

  payload = "src="+data
  
  if lan=='hi':
    payload = payload + "&hl=hi-in&v=Kabir&r=1&c=mp3&f=44khz_16bit_stereo"
  else:
    payload = payload + "&hl=en-us&v=Mary&r=0&c=mp3&f=44khz_16bit_stereo"

  headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "voicerss-text-to-speech.p.rapidapi.com",
    'x-rapidapi-key': os.environ.get('X_RAPIDAPI_KEY')
  }

  response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

  return response

@csrf_exempt
def TextToVoice(request):
  text = json.loads(request.body).get("text")

  soup = BeautifulSoup(text, "html.parser")
  text = soup.get_text()
  text = quote(text)

  lan = request.COOKIES.get('lan','en')
  voice = Voice(text,lan)

  return HttpResponse(voice, content_type='audio/mp3')

def Scholarship_API(request):
  data = getScholarships()
  for i in data:
    i.pop('color', None)
    i.pop('closing_date_print', None)
    i['closing_date'] = i['closing_date'].strftime("%d %b %Y")
  data = json.dumps(data, indent=4, sort_keys=True, default=str)
  return HttpResponse(data, content_type="application/json")

def Employment_API(request):
  data = getEmployment()
  data = json.dumps(data, indent=4, sort_keys=True, default=str)
  return HttpResponse(data, content_type="application/json")

def Social_API(request):
  data = getSocial()
  data = json.dumps(data, indent=4, sort_keys=True, default=str)
  return HttpResponse(data, content_type="application/json")

def Women_API(request):
  data = getWomen()
  data = json.dumps(data, indent=4, sort_keys=True, default=str)
  return HttpResponse(data, content_type="application/json")