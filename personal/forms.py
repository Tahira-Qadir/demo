from django import forms  
from .models import UserRole  

# user role form
class UserRoleForm(forms.ModelForm):  
    class Meta:  
        model = UserRole 
        fields = "__all__"  