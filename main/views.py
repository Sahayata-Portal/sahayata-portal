from django.shortcuts import render, HttpResponse
from main.models import *
from django.shortcuts import render
from .forms import *
from main.fetches import *
import random
from django.template.loader import render_to_string
from main.api import *
from main.templatetags.filters import translate

def HomePage(request):

  return render(request,"main/home.html")


def SchemePage(request):

  schemes = Scheme.objects.all()

  return render(request,"main/schemes.html",{"schemes":schemes})

def Ourteam(request):

  return render(request,"main/ourteam.html")


def Scholarships(request):

  schemes = getScholarships()

  lan = request.COOKIES.get('lan','en') 
  x = []
  for i in range(len(schemes)):
    x.append(schemes[i]['name'])
  x=TranslateList(x,lan)
  c=0
  for i in range(len(schemes)):
    schemes[i]['name']=x[c]
    c = c+1

  return render(request,"main/scholarships.html",{"data":schemes, "lan":lan})

def international(request):

  schemes = getScholarships()

  return render(request,"main/international.html",{"data":schemes})

def about(request):
  
  return render(request,"main/about.html")

def Employment(request):

  schemes = getEmployment()

  lan = request.COOKIES.get('lan','en') 
  x = []
  for i in range(len(schemes)):
    x.append(schemes[i]['title'])
    x.append(schemes[i]['head1'])
    for j in range(len(schemes[i]['desc1'])):
      x.append(schemes[i]['desc1'][j])
    x.append(schemes[i]['head2'])
    for j in range(len(schemes[i]['desc2'])):
      x.append(schemes[i]['desc2'][j])
  x=TranslateList(x,lan)
  c=0
  for i in range(len(schemes)):
    schemes[i]['title']=x[c]
    c = c+1
    schemes[i]['head1']=x[c]
    c = c+1
    for j in range(len(schemes[i]['desc1'])):
      schemes[i]['desc1'][j]=x[c]
      c=c+1
    schemes[i]['head2']=x[c]
    c = c+1
    for j in range(len(schemes[i]['desc2'])):
      schemes[i]['desc2'][j]=x[c]
      c=c+1
  
  return render(request,"main/Employment.html",{"data":schemes})

def social(request):

  schemes = getSocial()
  
  lan = request.COOKIES.get('lan','en') 
  x = []
  for i in range(len(schemes)):
    x.append(schemes[i]['title'])
    for j in range(len(schemes[i]['desc1'])):
      x.append(schemes[i]['desc1'][j])
    x.append(schemes[i]['head2'])
    for j in range(len(schemes[i]['desc2'])):
      x.append(schemes[i]['desc2'][j])
    x.append(schemes[i]['head3'])
    for j in range(len(schemes[i]['desc3'])):
      x.append(schemes[i]['desc3'][j])
  x=TranslateList(x,lan)
  c=0
  for i in range(len(schemes)):
    schemes[i]['title']=x[c]
    c = c+1
    for j in range(len(schemes[i]['desc1'])):
      schemes[i]['desc1'][j]=x[c]
      c=c+1
    schemes[i]['head2']=x[c]
    c = c+1
    for j in range(len(schemes[i]['desc2'])):
      schemes[i]['desc2'][j]=x[c]
      c=c+1
    schemes[i]['head3']=x[c]
    c = c+1
    for j in range(len(schemes[i]['desc3'])):
      schemes[i]['desc3'][j]=x[c]
      c=c+1

  return render(request,"main/social.html",{"data":schemes})

def subscribe(request):
  lan = request.COOKIES.get('lan','en') 
  MSG=''
  Type=1
  form = EmailForm()
  if request.method == 'POST':
    if request.POST.get('type')=='1':
      email = request.POST.get("Email")
      if len(MailForm.objects.filter(Email=email))==0:
        MailForm(Email=request.POST.get("Email"),  Name="").save()
      cur = MailForm.objects.filter(Email=email)[0]
      cur.OTP = str(random.randint(100000, 999999))
      cur.Tries = 0
      cur.save()
      mail = render_to_string('main/otp.html', {'otp':str(cur.OTP)})
      send_mail('OTP for Sahayata Portal verification','','Sahayata Portal <'+settings.EMAIL_HOST_USER+'>',[email],html_message=mail)
      if lan=='hi':
        MSG = translate(request,'OTP')+" "+email+translate(request,' sent to')
      elif lan=='en':
        MSG = 'OTP sent to '+email

      form = OTPForm({'email':email})
      Type=2

    elif request.POST.get('type')=='2':
      email=request.POST.get("email")
      otp=request.POST.get("OTP")
      try:
        temp = MailForm.objects.get(Email=email)
        if otp == temp.OTP:
          form = SubsForm(instance=temp)
          Type = 3
        else:
          tries = temp.Tries
          if tries==2:
            MSG = translate(request,'Incorrect OTP entered 3 times !')
          else:
            if lan=='hi':
              MSG = 'आपने गलत ओटीपी डाला है। आपके पास ' + str(2-tries) + ' कोशिशें बाकी हैं।'
            elif lan=='en':
              MSG = 'Incorrect OTP ! ' + str(2-tries) + ' tries left'
            MailForm.objects.filter(Email=email).update(Tries=tries+1)
            form = OTPForm({'email':request.POST.get("email")})
            Type=2
      except:
        pass
      
    elif request.POST.get('type')=='3':
      email=request.POST.get("Email")
      otp=request.POST.get("OTP")
      temp = MailForm.objects.filter(Email=email).filter(OTP=otp)
      if len(temp)>0:
        temp=temp[0]
        thisform = SubsForm(request.POST, instance=temp)
        thisform.save()
        MailForm.objects.filter(Email=email).filter(OTP=otp).update(Active=True)
        MSG = translate(request,'Data updated')
      else:
        MSG = translate(request,'Error updating data, please try again')

    else:
      MSG=translate(request,'Invalid form submission !')

  return render(request, 'main/subscribe.html', {'form':form, 'msg':MSG, 'type':Type, 'form_head':'Subscribe to email notifications'})

def Unsubscribe(request, uuid):
  obj = []
  try:
    obj = MailForm.objects.filter(UUID=uuid)
  except:
    pass
  if len(obj)==0:
    return render(request,"main/unsubscribe.html",{"msg":'You are already unsubscribed'})
  if request.method == 'POST':
    obj.delete()
    return render(request,"main/unsubscribe.html",{"msg":'You are successfully unsubscribed'})
  
  return render(request,"main/unsubscribe.html",{"ask":1})

def Update(request, schemetype):
  if schemetype=="scholarship":
    updateScholarships()

  return HttpResponse("OK")

def Women(request):
  
  schemes = getWomen()

  lan = request.COOKIES.get('lan','en') 
  x = []
  for i in range(len(schemes)):
    x.append(schemes[i]['name'])
  x=TranslateList(x,lan)
  c=0
  for i in range(len(schemes)):
    schemes[i]['name']=x[c]
    c = c+1

  return render(request,"main/Women.html",{"data":schemes, "lan":lan})
