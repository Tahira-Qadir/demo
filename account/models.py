from django.db import models
from personal.models import UserRole
from courses.models import Course
from django.core.exceptions import ValidationError

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE, related_name='user_role')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_title')
    is_deleted = models.BooleanField(default=False)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False) 
    date_joined =  models.DateTimeField(auto_now_add=True)  # Automatically set when object is created
    last_login =  models.DateTimeField(auto_now=True) 
    password1 = models.CharField(max_length=128)  
    password2 = models.CharField(max_length=128)
    
    
    
    def __str__(self):
        return self.username
