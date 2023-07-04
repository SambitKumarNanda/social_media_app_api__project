from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser


# Create your models here.

class CustomBaseManager(BaseUserManager):

    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email field is required")

        email = self.normalize_email(email)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_employee", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email field is required")

        email = self.normalize_email(email)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_employee", False)
        extra_fields.setdefault("is_active", False)
        extra_fields.setdefault("is_superuser", True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)

    # Permissions for the default user model
    is_active = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomBaseManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
