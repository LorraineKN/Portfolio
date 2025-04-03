from django.db import models
from django.utils.text import slugify


# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.CharField(max_length=100)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='cover_images/', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts')
    tags = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    