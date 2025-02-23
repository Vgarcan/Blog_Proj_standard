from django.contrib import admin
from .models import Category, Tag, Author, Post, Comment

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'created_at',
                    'updated_at', 'times_visited')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at',
                    'updated_at', 'times_visited')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    # list_filter = ('created_at', 'updated_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'category',
                    'created_at', 'updated_at', 'times_visited', 'is_published')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'author__name', 'category__name')
    list_filter = ('created_at', 'updated_at',
                   'author', 'category', 'is_published')
    filter_horizontal = ('tags',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'content',
                    'created_at', 'updated_at', 'is_approved')
    search_fields = ('author', 'post__title')
    list_filter = ('created_at', 'updated_at', 'post', 'is_approved')
