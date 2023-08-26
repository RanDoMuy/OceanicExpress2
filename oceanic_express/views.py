from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import package, signupcred, logincred
# Create your views here.

def home(requests):
    #signup
    if requests.method== "POST":
        try:
            tracking_id= requests.POST['tracking_id']
            packageinfo= package.objects.get(Tracking_Id= tracking_id)
            return render(requests, "packagedetails.html", {"packageinfo": packageinfo})
        except:
            redirect("home")
        
    return render(requests, "index.html", {})


def signups(requests):
    if requests.method== "POST":    
        fullname= requests.POST['fullname']
        email= requests.POST['email']
        number= requests.POST['number']
        password= requests.POST['password']

        newusercred= signupcred(
            Fullname= fullname,
            Email= email, 
            Number= number,
            Password= password)
        newusercred.save()

        return redirect("home")
    
    return render(requests, "signup.html", {})

def logins(requests):
    if requests.method== "POST":
        email= requests.POST['email']
        password= requests.POST['password']

        usercred= logincred(
            Email= email,
            Password= password)
        usercred.save()

        return redirect("home")
    
    return render(requests, "login.html", {})

def terms(requests):
    return render(requests, "terms.html", {})

def privacy(requests):
    return render(requests, "privacypolicy.html", {})

