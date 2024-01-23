from django.db import models

from accounts.models import CustomUser
from django_ckeditor_5.fields import CKEditor5Field

STATUS = (
    (0,'Draft'),
    (1, 'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200,unique=True)
    body = CKEditor5Field('Text', config_name='extends')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    