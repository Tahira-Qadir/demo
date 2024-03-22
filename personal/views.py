from django.shortcuts import get_object_or_404, render, redirect  
from .forms import UserRoleForm  
from .models import UserRole 
# Create your views here.  


def show_list(request):  # Get all the objects in the table
    user_roles =  UserRole.objects.all()  
    return render(request, 'personal/show_list.html', {
        'user_roles':user_roles,
    })


def create(request):  # Can edit seleted user
    if request.method == 'POST':
        form = UserRoleForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('show_list')  # Redirect to the all list of the user
    else:
        form = UserRoleForm()
    return render(request, 'personal/create.html', {'form': form})  # render to the create user page


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


def delete(request, user_id):  # Can delete seleted user
    user_role = UserRole.objects.get(pk=user_id) 
    if request.method == 'POST':
        user_role.delete() 
        return redirect('show_list')
    
    return render(request, 'personal/delete.html', {'user_role':user_role})  # render to the delete user page