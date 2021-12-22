from django.shortcuts import render
from django.views.generic import View

class FrontEndRenderView(View):
    def get(self,request,*args,**kwargs):
        return render('main/main.html',{})


# Create your views here.
