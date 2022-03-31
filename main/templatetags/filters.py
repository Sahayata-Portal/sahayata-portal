from django import template

register = template.Library()

@register.simple_tag
def print_date(dt):
  return dt.strftime("%d-%b-%Y")