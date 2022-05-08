from django import template
from main.locale import trans

register = template.Library()

@register.simple_tag
def print_date(dt):
  return dt.strftime("%d-%b-%Y")

@register.simple_tag
def translate(request, text):
  lan = request.COOKIES.get('lan','en') 
  try:
    if lan=="en":
      return trans[text][0]
    elif lan=="hi":
      return trans[text][1]
  except:
    return text