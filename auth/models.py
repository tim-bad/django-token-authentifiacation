from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',
            max_length=255,
            unique=True,
             )
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    USERNAME_FIELD = 'email'


