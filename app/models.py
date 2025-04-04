from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class BaseModel(models.Model):
    """Abstract base model with common fields"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, max_length=200)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_source = getattr(self, 'slug_source', 'name')
            self.slug = slugify(getattr(self, slug_source))
        super().save(*args, **kwargs)


class SluggedModel(BaseModel):
    """Abstract model for objects that use name and slug fields"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(SluggedModel):
    class Meta(SluggedModel.Meta):
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Tag(SluggedModel):
    class Meta(SluggedModel.Meta):
        pass

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})


class Post(BaseModel):
    title = models.CharField(max_length=200)
    slug_source = 'title'  # Tells BaseModel what field to use for slug generation
    content = models.TextField()
    summary = models.TextField(
        max_length=300,
        blank=True,
        help_text="A brief summary of the post (optional)"
    )
    cover_image = models.ImageField(
        upload_to='posts/cover_images/%Y/%m/%d/',
        blank=True,
        null=True,
        help_text="Upload a cover image (optional)"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='posts',
        blank=True
    )
    published_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Set date and time to publish this post"
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Mark this post as featured"
    )

    class Meta:
        ordering = ['-published_at']
        get_latest_by = "published_at"
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    @property
    def is_published(self):
        return self.published_at is not None