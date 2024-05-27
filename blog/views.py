from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse

from .models import Post, Categories
from .forms import PostForm, PostUpdateForm

def home(request):
    posts = Post.objects.filter(status=1)
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)
    
class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'post/post_list_view.html'

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post/post_detail_view.html'

class CategoryView(DetailView):
    model = Categories
    template_name = 'post/categories_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = self.get_object()
        print(category)
        posts = Post.objects.filter(category=category)
        post_count = len(posts)

        context ={
            'posts':posts,
            'total_post':post_count,
            'category':category,
        }

        return context
    
class PostCreateView(CreateView):  
    model = Post
    form_class = PostForm
    template_name = 'post/post_create_view.html'
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug':self.object.slug})
    
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'post/post_update_view.html'
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug':self.object.slug})