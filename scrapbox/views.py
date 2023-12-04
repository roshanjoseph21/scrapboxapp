from django.shortcuts import render,redirect
from django.views.generic import View
from scrapbox.forms import UserForm,LoginForm
from django.contrib.auth import authenticate,login

# Create your views here.

class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=UserForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=UserForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            print("Success.....")
            return redirect("signin")
        else:
            return render(request,"register.html",{"form":form})
        

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                print("valid")
                return redirect("signin")
            print("invalid")
            return render (request,"login.html",{"form":form})