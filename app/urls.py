from django.contrib import admin
from django.urls import path
from app.views import index, dashboard, generating_report, loginuser, logoutuser

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('generating_report', generating_report, name='generating_report'),


    path('loginuser', loginuser, name='loginuser'),
    path('logoutuser', logoutuser, name='logoutuser'),
]
