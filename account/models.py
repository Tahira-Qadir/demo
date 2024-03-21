# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from personal.models import UserRole

# class MyAccountManager(BaseUserManager):
#     def  create_user(self, email, username, role, is_staff, is_active, password=None):
        
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not username:
#             raise ValueError('Users must have an username')
#         user = self.model(
#             email = self.normalize_email(email),
#             username = username,
#             role=role,
#             staf=is_staff,
#             active=is_active
#         )
        
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self,  email, username, role, password):
        
#         role = UserRole.objects.get(role_choices=1)
#         user = self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password,
#         )

#         user.is_staff = True
#         user.is_active = True
#         user.is_superuser = True
#         user.role = role
#         user.save(using=self._db)
#         return user
    
# class Account(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=50, unique=True)

#     # required
#     date_joined =  models.DateTimeField(auto_now_add=True)
#     last_login =  models.DateTimeField(auto_now_add=True)
#     role = models.ForeignKey(UserRole, on_delete=models.CASCADE, related_name='user_role', null=True)
#     is_deleted = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username',]
   
#     objects = MyAccountManager()

#     def __str__(self):
#         return self.email
    
#     def has_perm(self, perm, obj=None):
#         return self.is_superuser
    
#     def has_module_perms(self, add_label):
#         return True
    
