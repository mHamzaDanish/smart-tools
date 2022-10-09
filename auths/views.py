from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

@login_required( login_url='login' ) 
def logout_(request):
    logout(request)
    return redirect('login')
    
def login(request):
    if request.method == 'GET':
        context = {}
        return render(request,'auths/login.html',context) 
    elif request.method == 'POST':
        username_ = request.POST['username']
        password_ = request.POST['password']
        user = authenticate(
            username = username_,
            password = password_)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        context = {}
        return render(request,'auths/login.html',context)
 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            # login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auths/signup.html', {'form': form})



