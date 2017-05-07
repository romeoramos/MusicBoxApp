from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
#from modules.Songs.models import Song


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):

        if not email:
            raise ValueError('You must introduce an email')
        email = self.normalize_email(email)

        user = self.model(email=email,
                          is_active=True, is_staff=is_staff,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(
            email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, models.Model):

    # unique, no se van a repetir
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=25)
    phone = models.CharField(max_length=22)
    email = models.EmailField(unique=True, max_length=50)
    sex = models.CharField(choices=(('F','Female'),('M','Male')), max_length=16,blank=True)
    #library = models.ManyToManyField(Song,blank=True)

    # intermediario entre trans de cada modelo, object managaer de cada modelo
    objects = UserManager()

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.name
