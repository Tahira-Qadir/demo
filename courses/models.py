from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField()
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when object is created
    updated_at = models.DateTimeField(auto_now=True)   # # Automatically updated every time object is saved
    
    def __str__(self):
        return self.title
    