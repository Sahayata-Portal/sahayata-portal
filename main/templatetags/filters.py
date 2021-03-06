from django import template
from main.locale import trans

register = template.Library()

@register.simple_tag
def print_date(dt):
  return dt.strftime("%d %b %Y")

@register.simple_tag
def translate(request, text):
  lan = request.COOKIES.get('lan','en') 
  return trans(text,lan)

@register.simple_tag
def get_url(request):
  url = request.scheme + "://" + request.META['HTTP_HOST']
  return url