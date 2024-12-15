from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from meroblog import settings 

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='Profile Picture', blank=True, null=True)
    bio = models.CharField(max_length=250, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.id)])

class Contact(models.Model):
    user_from = models.ForeignKey(
            settings.AUTH_USER_MODEL, 
            related_name = 'rel_from_set',
            on_delete=models.CASCADE)
    user_to = models.ForeignKey(
            settings.AUTH_USER_MODEL, 
            related_name = 'rel_set_to',
            on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
                models.index(fields=['-created']),
                ]

    ordering = ['-created']

    def __str__(self):
        return f'{self.user_from} follow {self.user_to}'
