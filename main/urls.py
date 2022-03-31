"""CP301G1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from main import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('scholarships', views.Scholarships, name='scholarships'),
    path('schemes', views.SchemePage, name='schemes'),
    path('ourteam', views.Ourteam, name='ourteam'),
    path('about', views.about, name='about'),
    path('Employment',views.Employment,name='Employment'),
    path('social',views.social,name='social'),
    path('texttovoice',views.TextToVoice,name='texttovoice'),
    path('subscribe',views.subscribe,name='subscribe'),
    path('update/<str:schemetype>',views.Update, name='update')
]
