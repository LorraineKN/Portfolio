from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Tag, Post

# List View for Categories
class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 10  # Optional, paginate if you have many categories

# Detail View for Category
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

# List View for Tags
class TagListView(ListView):
    model = Tag
    template_name = 'tag_list.html'
    context_object_name = 'tags'
    paginate_by = 10  # Optional, paginate if you have many tags

# Detail View for Tag
class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag_detail.html'
    context_object_name = 'tag'

# List View for Blog Posts
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10  # Optional, paginate if you have many posts
    ordering = ['-published_at']  # Sort posts by published date in descending order

# Detail View for Post
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

