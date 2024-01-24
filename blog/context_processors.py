from .models import Categories
from django.contrib.auth import get_user_model

def categories_processor(request):
    categories = Categories.objects.all()
    return {
        'categories':categories,
    }