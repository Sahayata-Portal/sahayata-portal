from django.shortcuts import render
from main.models import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime


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

  count=0
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

  return render(request,"main/Employment.html")