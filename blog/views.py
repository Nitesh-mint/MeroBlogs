from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Post, Categories


def home(request):
    
    return render(request, 'home.html')
    

class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'post/post_list_view.html'
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post/post_detail_view.html'