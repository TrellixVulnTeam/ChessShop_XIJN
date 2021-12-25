from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('<pk:int>/', views.get_account, name='index'),
     path('register/',views.register,name ='register')
 ]