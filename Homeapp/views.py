from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *
from .forms import ConsoleListingForm

# Create your views here.

def home(request):
    return render(request,'Homeapp/home.html') 
def loginpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        validate_user=authenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('home')
        else:
            messages.error(request,'wrong user details or user does not exists')
            return redirect('loginpage')
    return render(request,'login/loginpage.html')


def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if len(password)<4:
            messages.error(request,'password too short')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request,"username already taken")
            return redirect('register')
        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        messages.success(request, 'User created successfully. login now')
        return redirect('loginpage')
    return render(request,'register/register.html')

def logout_view(request):
    logout(request)
    return redirect ('home')

@login_required
def create_listing(request):
    if request.method=='POST':
        form=ConsoleListingForm(request.POST,request.FILES)
        if form.is_valid():
            listing=form.save(commit=False)
            listing.user=request.user
            listing.save()
            return redirect('home')
    else:
        form=ConsoleListingForm()
    return render(request,'listing/create_listing.html',{'form':form})
    
