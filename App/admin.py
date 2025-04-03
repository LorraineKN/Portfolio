from django.contrib import admin
from .models import Post, category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published')
    search_fields = ('title', 'author', 'content')
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
#     {