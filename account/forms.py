from django import forms
from account.models import Account
from django.contrib.auth import authenticate
from django.contrib.auth.forms import  UserCreationForm

# Registration Form
class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

# Login Form
class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username'] 
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid Login")

 