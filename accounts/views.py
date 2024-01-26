from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import DetailView

from .models import CustomUser

class ProfileDetailView(DetailView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'account/profile.html'
        