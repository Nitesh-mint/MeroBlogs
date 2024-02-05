from django.db import models

from accounts.models import CustomUser
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse

STATUS = (
    (0,'Draft'),
    (1, 'Publish')
)

class Categories(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250,unique=True, help_text="This will be auto populated")


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.slug)])

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200,unique=True, help_text="Url of the post") 
    thumbnail = models.ImageField(upload_to='Post Thumbnails', null=True, blank=True, help_text="This is a image field to show the image in the list and in the beginning of the post")
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, null=True, blank=True) # Do not let category to be deleted until there is Post related to it!  
    body = CKEditor5Field('Text', config_name='extends')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.slug)])
    