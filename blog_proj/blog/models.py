from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='subcategories',
        null=True,
        blank=True
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    times_visited = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.slug])

    def get_children(self):
        return Category.objects.filter(parent=self)

    def get_parent(self):
        return self.parent if self.parent else None

    def save(self):
        self.slug = slugify(self.name)
        super().save()

    def increase_visit_count(self):
        self.times_visited += 1
        self.save()


class Tag (models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    times_visited = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tags"

    def save(self):
        self.slug = slugify(self.name)
        self.name = self.name.lower()
        super().save()

    def increase_visit_count(self):
        self.times_visited += 1
        self.save()


class Author(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Authors"

    def save(self):
        self.slug = slugify(self.name)
        self.name = self.name.lower()
        self.email = self.email.lower()
        super().save()


class Post(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    times_visited = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def get_tags(self):
        return self.tags.all()

    def save(self):
        self.slug = slugify(self.title)
        super().save()
        self.title = self.title.lower()
        super().save()

    def increase_visit_count(self):
        self.times_visited += 1
        self.save()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'

    def approve(self):
        self.is_approved = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.post.slug])

    class Meta:
        verbose_name_plural = "Comments"

    def get_author(self):
        return self.author.capitalize()

    def get_post_title(self):
        return self.post.title
