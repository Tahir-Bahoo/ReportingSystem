from django.contrib import admin
from django.urls import path
from app.views import index, generating_report

urlpatterns = [
    path('', index, name='index'),
    path('generating_report', generating_report, name='generating_report'),
]
