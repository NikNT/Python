from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def index(req):
    # if req.user.is_authenticated:
    #     return redirect('/login')
    # return HttpResponse('This is Index')
    return render(req, 'index.html')

def loginUser(req):
    # return HttpResponse('This is login')
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')
        # Check for credentials 
        user = authenticate(username=username, password=password)
        if user is not None: 
            login(req, user)
            return redirect("/")
        else: 
            return render(req, 'login.html') 
    return render(req, 'login.html')

def logoutUser(req):
    logout(req)
    # return HttpResponse('This is logout')
    return redirect('/login')