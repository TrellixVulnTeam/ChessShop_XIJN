from django.db.models.fields import json
from django.shortcuts import redirect, render 
from . import models
from .forms import CreateUserForm
from main import urls
from django.http import JsonResponse

# Create your views here.
def get_account(request,id):
    user = models.UserAccount.objects.get(id = id)
    return user

def register(request):
    if request.method == "POST":
        newUser = CreateUserForm(request.method.POST)
        if newUser.is_valid():
            newUser.save()
            redirect('main-index')
    context = {"form":newUser}
    render(request,'header.html',context)
    return JsonResponse(newUser,safe = False)