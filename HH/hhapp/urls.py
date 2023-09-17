from django.contrib import admin
from django.urls import path, include
import HH.hhapp.views
from HH.hhapp import views

app_name = 'hhapp'

urlpatterns = [
    path('', views.start, name='index'),
    path('form/', views.form, name='form'),
    path('result/', views.result, name='result')
]
