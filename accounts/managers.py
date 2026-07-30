from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    # Indicates that this manager should be used when creating migrations for the User model.
    use_in_migrations = True  
    
    # Sets the default values for the fields is_staff and is_superuser to False and calls the _create_user method to create a user.
    def create_user(self, uid, password = None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        
        return self._create_user(uid, password, **extra_fields)
    
    # Creates a User with all fields and set hashed password. Main User Creator Function.
    def _create_user(self, uid, password, **extra_fields):
        if not uid: raise ValueError("The UID must not be Empty")
        if not password: raise ValueError("The Password must not be Empty")
        email = extra_fields.get("email")
        if email: extra_fields["email"] = self.normalize_email(email)
        user = self.model(uid = uid, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        
        return user
    
    # Create a superuser by setting the default values for the fields is_staff and is_superuser to True and calls the _create_user method to create a superuser.
    def create_superuser(self, uid, password = None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_staff") is not True: raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True: raise ValueError("Superuser must have is_superuser=True.")
        
        return self._create_user(uid, password, **extra_fields)
    
    