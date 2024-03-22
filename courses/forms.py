from django import forms  
from .models import Course  

# Course form
class CourseForm(forms.ModelForm):
    class Meta:  
        model = Course 
        fields = "__all__"  