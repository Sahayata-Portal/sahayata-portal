from django.shortcuts import render
from main.models import *

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