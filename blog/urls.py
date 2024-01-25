from django.urls import path

from .views import PostDetailView, home, PostListView, CategoryView

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:slug>/',CategoryView.as_view(), name='category_detail'),
    path('post/',PostListView.as_view(),name='post_list'),
    path('post/<slug:slug>/',PostDetailView.as_view(), name='post_detail'),
]