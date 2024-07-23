from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField("Никнейм", max_length=50, unique=True)
    email = models.EmailField("Почта", unique=True)
    age = models.PositiveIntegerField("Возраст",null=True, blank=True)
    phone = models.CharField("Номер телефона",max_length=20,null=True, blank=True)
    address = models.TextField("Адрес",null=True, blank=True)
    avatar = models.ImageField("Аватарка",upload_to='avatars/', null=True, blank=True)

    objects = UserManager()