"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blogs import views
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.img_predict),
    path('statistic/', views.get_statistic),
    path('login/', views.login),
    path('patients/', views.patients),
    path('patient/information/', views.patient_information),
    path('patients/risk/', views.patients_risk),
    path('patients/normal/', views.patients_normal),
    path('medtech/submit/', views.medtech_submit),
    path('medical/undiagnosed/', views.undiagnosed),
    path('medical/diagnosed/', views.diagnosed),
    path('medical/submit/', views.medical_submit),
    path('patient/add/', views.patient_add),
    path('patient/edit/', views.patient_edit),
    path('patient/remove/', views.patient_remove),
    path('prediction/', views.img_predict),
    path('home/', views.get_statistic),

]
