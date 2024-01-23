from django.shortcuts import render
from django.views.generic import DetailView

from .models import Post

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post/post_detail_view.html'