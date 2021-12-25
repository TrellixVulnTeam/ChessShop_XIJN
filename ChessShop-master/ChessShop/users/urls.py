from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('login/', views.login_api, name='index'),
     path('register/',views.register_api,name ='register')
 ]