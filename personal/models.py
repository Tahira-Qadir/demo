from django.db import models

class UserRole(models.Model): 
    role_choices = (
        (1, 'Admin'),
        (2, 'Teacher'),
        (3, 'Student'),
    )
    role = models.PositiveSmallIntegerField(choices=role_choices)
    description = models.TextField(null=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when object is created
    updated_at = models.DateTimeField(auto_now=True)   # # Automatically updated every time object is saved

    def __str__(self):
        for role_id, role_name in self.role_choices:
            if self.role == role_id:
                return role_name
   

