from django.db import models
from django.contrib.auth.models import User

class UserRole(models.Model): 
    role_choices = (
        (1, 'Admin'),
        (2, 'Teacher'),
        (3, 'Student'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=role_choices)
    contact = models.CharField(max_length=15)
    adress = models.TextField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when object is created
    updated_at = models.DateTimeField(auto_now=True)   # # Automatically updated every time object is saved

    def __str__(self):
        for role_id, role_name in self.role_choices:
            if self.role == role_id:
                return role_name


