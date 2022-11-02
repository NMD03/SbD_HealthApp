from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from fileshare.models import *
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}!')
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'users/login.html')
    else:
        return render(request, 'users/login.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
        if password == password2:
            if len(password) < 8:
                messages.info(request, 'Password must be at least 8 characters')
                return redirect('register')
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            group = Group.objects.get(name='patient')
            user.groups.add(group)
            Patient.objects.create(
                user=user
            )
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return render(request, 'users/register.html')
    else:
        return render(request, 'users/register.html')

