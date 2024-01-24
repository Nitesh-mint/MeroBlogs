from django.urls import path

from .views import PostDetailView, home, PostListView

urlpatterns = [
    path('', home, name='home'),
    path('post/',PostListView.as_view(),name='post_list'),
    path('post/<slug:slug>/',PostDetailView.as_view(), name='post_detail'),
]