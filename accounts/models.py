from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='Profile Picture', blank=True, null=True)
    bio = models.CharField(max_length=250, blank=True, null=True)