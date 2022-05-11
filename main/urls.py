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
from main import views,api

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('scholarships', views.Scholarships, name='scholarships'),
    path('international', views.international, name='international'),
    path('schemes', views.SchemePage, name='schemes'),
    path('ourteam', views.Ourteam, name='ourteam'),
    path('about', views.about, name='about'),
    path('Employment',views.Employment,name='Employment'),
    path('social',views.social,name='social'),
    path('texttovoice',api.TextToVoice,name='texttovoice'),
    path('subscribe',views.subscribe,name='subscribe'),
    path('unsubscribe/<str:uuid>',views.Unsubscribe,name='unsubscribe'),
    path('update/<str:schemetype>',views.Update, name='update'),
    path('Women',views.Women,name='Women'),
    path('api/scholarships',api.Scholarship_API,name="scholarship_api"),
    path('api/employment',api.Employment_API,name="employment_api"),
    path('api/social',api.Social_API,name="social_api"),
    path('api/women',api.Women_API,name="women_api"),
]
