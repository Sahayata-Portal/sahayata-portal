import requests
import json
import os
from main.models import Translations

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
    text = text + i + "   ###\n###   "

  translated = Translate(text, lan)

  translated = translated.split("###\n###")[:-1]
  for i in range(len(translated)):
    translated[i].strip()

  return translated