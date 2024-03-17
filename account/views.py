from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import RegistrationForm, AccountAuthenticationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


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

def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form =  AccountAuthenticationForm()
    return render(request,'account/login.html', {
            'form' : form
        })

def  logout_view(request):
    logout(request)
    return redirect('login')
