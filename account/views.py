from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from .forms import UserCreationForm, UserLoginForm
from django.http import HttpResponse
from .models import User
# Create your views here. 

# Home page
def home(request):
    return render(request, 'home.html')

def user_list(request):  # Get all the objects in the table
    user_lists =  User.objects.all()  
    return render(request, 'account/user_list.html', {
        'user_lists':user_lists,
    })


def create_user(request):  # Can edit seleted user
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        try:
            if form.is_valid():
                form.save()  # Save the form data to the database
                return redirect('user_list')  # Redirect to the all list of the user
        except ValueError as e:
            return  HttpResponse(str(e))
    else:
        form = UserCreationForm()
    return render(request, 'account/create.html', {'form': form})  # render to the create user page


def update_user(request, user_id): # Can update seleted user
    user_roles = get_object_or_404(User, pk=user_id) 
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=user_roles)  
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserCreationForm(instance=user_roles)  
    return render(request, 'account/update.html', {'form': form})  # render to the update user page


def delete_user(request, user_id):  # Can delete seleted user
    user_roles = User.objects.get(pk=user_id) 
    if request.method == 'POST':
        user_roles.delete() 
        return redirect('user_list')
    
    return render(request, 'account/delete.html', {'user_roles':user_roles})  # render to the delete user page

# Registration 
def register_view(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('login')
    else:
            form = UserCreationForm()
    return render(request, 'account/register.html', {
        'form':form
        })

# Login
def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form =  UserLoginForm()
    return render(request,'account/login.html', {
            'form' : form
        })
    
# Logout
def  logout_view(request):
    logout(request)
    return redirect('login')
