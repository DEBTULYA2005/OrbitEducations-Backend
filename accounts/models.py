from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import UserManager 

class User(AbstractBaseUser, PermissionsMixin):
    
    uid = models.CharField(max_length=32, unique=True, db_index=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    parent_name = models.CharField(max_length=150, blank=True)
    parent_phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    enrolled_course = models.ForeignKey(
        "courses.Course",
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="enrolled_students",
    )
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    # Custom User Manager: whenever we want to create, we can use simply UserManger as "objects".
    objects = UserManager()
    
    USERNAME_FIELD = "uid"
    REQUIRED_FIELDS = ["email", "name", "phone"]
    
    def __str__(self):
        return f"{self.uid}, {self.name}, {self.email}"