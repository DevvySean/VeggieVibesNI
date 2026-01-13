from django.contrib import admin
from .models import Category, Post, Reply, UserProfile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_at', 'views', 'is_pinned']
    list_filter = ['category', 'is_pinned', 'created_at']
    search_fields = ['title', 'content', 'author__username']
    date_hierarchy = 'created_at'


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content', 'author__username', 'post__title']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'joined_date']
    search_fields = ['user__username', 'location']
