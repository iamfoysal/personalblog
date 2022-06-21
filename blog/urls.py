from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView,UserPostListView,  PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]