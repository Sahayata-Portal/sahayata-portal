from django.shortcuts import render
from main.models import *
import requests
from bs4 import BeautifulSoup


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
      closing_date.get_text(strip=True),
      'https://scholarships.gov.in'+guideline.a.attrs['href'],
      'https://scholarships.gov.in'+faq.a.attrs['href']])



  return render(request,"main/scholarships.html",{"data":schemes})