from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from fileshare.models import *
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from verify_email.email_handler import send_verification_email

from .forms import *
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
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            username = inactive_user.username
            group = Group.objects.get(name='patient')
            inactive_user.groups.add(group)
            Patient.objects.create(
                user=inactive_user
            )
            messages.success(request, f'Hello {username}.We have sent you an email to verify your Account!')
            return redirect('login')
    
    context = {'form': form}
    return render(request, 'users/register.html', context)

