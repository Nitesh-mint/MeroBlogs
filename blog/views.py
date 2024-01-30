from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Post, Categories

def home(request):
    posts = Post.objects.all()
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