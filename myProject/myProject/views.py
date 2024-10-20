from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from myApp.models import *
from myProject.forms import *

from django.contrib import messages


def loginPage(request):
    
    if request.method == 'POST':
        loginform=myAuthencationForm(request,data=request.POST)
        
        if loginform.is_valid():
            user=loginform.get_user()
            login(request,user)
            return redirect("dashboardPage")
        
    else:
        loginform=myAuthencationForm()
    
    context ={
        'loginform': loginform
    }
        
    
    return render(request,'loginPage.html',context)



def registerPage(request):
    if request.method == 'POST':
        form=myUserCreationForm(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.success(request,"Register Successfilly")
            return redirect("loginPage")
        
    else:
        form=myUserCreationForm(request.POST)
        
    context={
        'form':form
    }
    
    return render(request,'registerPage.html',context)

@login_required
def dashboardPage(request):
    
    return render(request,"dashboardPage.html")

@login_required
def logoutPage(request):
    logout(request)
    return redirect("loginPage")
    

