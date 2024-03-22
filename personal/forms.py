from django import forms  
from .models import UserRole  

# user role form
class UserRoleForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)  
    class Meta:  
        model = UserRole 
        fields = "__all__"  