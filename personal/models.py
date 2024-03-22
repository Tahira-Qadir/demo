from django.contrib.auth.hashers import make_password
from django.db import models
from courses.models import Course

class UserRole(models.Model): 
    role_choices = (
        (1, 'Admin'),
        (2, 'Teacher'),
        (3, 'Student'),
    )
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    role = models.PositiveSmallIntegerField(choices=role_choices)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=15)
    adress = models.TextField()
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when object is created
    updated_at = models.DateTimeField(auto_now=True)   # # Automatically updated every time object is saved
    password1 = models.CharField(max_length=128)  
    password2 = models.CharField(max_length=128)  

    def save(self, *args, **kwargs):
        if self.password1 != self.password2:
            raise ValueError("Passwords do not match")
        else:
            self.password1 = make_password(self.password1)
        super().save(*args, **kwargs)
    

    def __str__(self):
        for role_id, role_name in self.role_choices:
            if self.role == role_id:
                return role_name
   

