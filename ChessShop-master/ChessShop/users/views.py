from django.shortcuts import redirect, render 
from . import models
from .forms import CreateUserForm
from main import urls

# Create your views here.
def get_account(request,id):
    user = models.UserAccount.objects.get(id = id)

def register(request):
    if request.method == "POST":
        newUser = CreateUserForm(method.POST)
        if newUser.is_valid():
            newUser.save()
            redirect('main-index')
    context = {"form":newUser}
    render(request,'header.html',context)