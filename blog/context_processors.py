from .models import Author, Categories
from django.contrib.auth import get_user_model

def author_processor(request):
    author = request.user
    if request.user.is_authenticated:
        author = Author.objects.get(user=request.user)
    return { 
        'author' : author,
            }

def categories_processor(request):
    categories = Categories.objects.all()
    return {
        'categories':categories,
    }