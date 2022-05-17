from django.db import models
from core.models import TimeStampedModel
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('email is required')
        if not password:
            raise ValueError('password is required')
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        superuser = self.create_user(
            email=email,
            password=password,
            **extra_fields
        )
        superuser.set_password(password)
        superuser.is_superuser = True
        superuser.is_admin = True
        superuser.is_staff = True
        superuser.save(using=self._db)
        return superuser


class User(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    """
    User Model
    """
    objects = UserManager()
    
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True, verbose_name='이메일')
    password = models.CharField(max_length=255, blank=True, null=True, verbose_name='비밀번호')
    
    # default
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    is_staff = models.BooleanField(default=False, verbose_name='스태프')
    is_admin = models.BooleanField(default=False, verbose_name='어드민')
    is_superuser = models.BooleanField(default=False, verbose_name='슈퍼유저')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name_plural = '1. 유저'
        db_table = 'users'
    
    def __str__(self):
        return str(self.email)