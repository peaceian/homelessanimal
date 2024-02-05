"""
URL configuration for homelessanimal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from animalapp import views #add define path
from django.urls import re_path
from animalapp import views
from animalapp.views import animal, crawlerall, animalpage, search

from django.contrib.staticfiles.storage import staticfiles_storage
#from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('hello/<str:username>',views.Sayhello),
    path('animalpage/',animalpage),#main page
    path('animalpage/<pageindex>/',animalpage),
    path('animal/<int:animal_id>/',animal),#define the addr and function()
    path('animals/',crawlerall),
    re_path(r'animalpage/(\d+)/$',views.animalpage,name="index"),
    #path('filter/',views.filter), #要導入 re_path 套件
    path('animalpage/',search),
    path('',animalpage),
   
    
]
