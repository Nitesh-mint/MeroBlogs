from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.utils.text import slugify

from .models import Post, Categories, PostLikes
from .forms import PostForm, PostUpdateForm

class Home(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'
    paginate_by = 5
    
    def get_template_names(self):
        if self.request.htmx:
            return ['post/post_list_htmx.html']
        return ['home.html']
class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'post/post_list_view.html'

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post/post_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        likes  =  PostLikes.objects.filter(post=self.get_object()).count()
        context['likes'] = likes

        return context



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

class PostCreateView(LoginRequiredMixin,CreateView):  
    model = Post
    form_class = PostForm
    template_name = 'post/post_create_view.html'
    
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug':self.object.slug})
    
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'post/post_update_view.html'
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug':self.object.slug})
    
def like_posts(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like, created = PostLikes.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()
    else:
        like.save()
    
    return HttpResponseRedirect(reverse('post_detail',kwargs={'slug':slug}))
