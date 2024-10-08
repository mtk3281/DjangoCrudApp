from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate
from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})


def mylogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm() 

    context = {'form': form}
    return render(request, 'registration/my-login.html', context=context)

#user logout
def user_logout(request):
    auth.logout(request)

    return redirect('')