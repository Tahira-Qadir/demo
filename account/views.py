from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from .forms import RegistrationForm, AccountAuthenticationForm

# Home page
def home(request):
    return render(request, 'home.html')

# Registration 
def register_view(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('login')
    else:
            form = RegistrationForm()
    return render(request, 'account/register.html', {
        'form':form
        })

# Login
def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form =  AccountAuthenticationForm()
    return render(request,'account/login.html', {
            'form' : form
        })
    
# Logout
def  logout_view(request):
    logout(request)
    return redirect('login')
