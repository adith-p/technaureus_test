from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .models import User

from .forms import *

# Create your views here.


def login_user(request):
    """
    This view is for logging in a Superuser.
    """
    if request.user.is_authenticated:
        return redirect('library_app:listAllAuthors')
    if request.method == 'POST':
        form = loginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(username = username)
            except User.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'User does not exist contact superuser')
                return redirect('user_auth:login_user')  

            if user.is_superuser:
                user = authenticate(request,username=username,password=password)
                if not user:
                    messages.add_message(request, messages.ERROR, 'username or password is wrong')
                    return redirect('user_auth:login_user')  
                login(request,user)
                return redirect('library_app:listAllAuthors')
            
            messages.add_message(request, messages.ERROR, 'Only admins are allowed to login')
            return redirect('user_auth:login_user') 
  
    return render(request,'user_auth/login.html')


def logout_user(request):

    logout(request)
    return redirect('user_auth:login_user')

