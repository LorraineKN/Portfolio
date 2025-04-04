from django.urls import path
from . import views

urlpatterns = [
    # List Views
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('posts/', views.PostListView.as_view(), name='post_list'),

    # Detail Views
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('tag/<slug:slug>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
]
