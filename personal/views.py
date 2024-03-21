from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect  
from django.http import Http404
from .forms import UserRoleForm  
from django.contrib.auth.models import User
from .models import UserRole  
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.  

@login_required
def show_list(request):  # Get all the objects in the table
    user_roles =  UserRole.objects.all()  
   
    return render(request, 'personal/show_list.html', {
        'user_roles':user_roles,
    })

@staff_member_required
def create(request):  # Can edit seleted user
    if request.method == 'POST':
        form = UserRoleForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('show_list')  # Redirect to the all list of the user
    else:
        form = UserRoleForm()
    return render(request, 'personal/create.html', {'form': form})  # render to the create user page

@staff_member_required
def update(request, user_id): # Can update seleted user
    user_role = get_object_or_404(UserRole, pk=user_id) 
    if request.method == 'POST':
        form = UserRoleForm(request.POST, instance=user_role)  
        if form.is_valid():
            form.save()
            return redirect('show_list')
    else:
        form = UserRoleForm(instance=user_role)  
    return render(request, 'personal/update.html', {'form': form})  # render to the update user page

@staff_member_required
def delete(request, user_id):  # Can delete seleted user
    user_role = UserRole.objects.get(pk=user_id) 
    if request.method == 'POST':
        user_role.delete() 
        return redirect('show_list')
    
    return render(request, 'personal/delete.html', {'user_role':user_role})  # render to the delete user page