from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='Profile Picture', blank=True, null=True)
    bio = models.CharField(max_length=250, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.id)])