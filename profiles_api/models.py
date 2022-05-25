from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_username(self,email,name,password=None):
        """create a new user profile"""
        if not email:
            raise ValueError("User must have emial address")

            email = self.normalize_email(email)
            user = self.model(email=email, name=name)

            user.set_password(password)
            user.save(using=self._db)

            return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = False
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractUser):
    """Database models for users in the system"""
    email = models.EmailField(max_length=500, unique=True)
    name = models.CharField(max_length=255)
    is_activate = models.BooleanField(max_length=255, default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FILED = 'email'
    REQUIRED_FIELD = ['name']

    def get_full_name(self):
        return self.name 

    def get_short_name(self):
        return self.name 

    def __str__(self):
        return self.email       