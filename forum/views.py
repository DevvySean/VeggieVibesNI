from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Post, Reply


def home(request):
    """Homepage showing all categories and recent posts"""
    categories = Category.objects.all()
    recent_posts = Post.objects.all()[:10]
    context = {
        'categories': categories,
        'recent_posts': recent_posts,
    }
    return render(request, 'forum/home.html', context)


def category_detail(request, slug):
    """Show all posts in a category"""
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all()
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'forum/category_detail.html', context)


def post_detail(request, post_id):
    """Show a post and its replies"""
    post = get_object_or_404(Post, id=post_id)
    post.views += 1
    post.save()
    replies = post.replies.all()
    
    context = {
        'post': post,
        'replies': replies,
    }
    return render(request, 'forum/post_detail.html', context)


@login_required
def create_post(request, slug):
    """Create a new post in a category"""
    category = get_object_or_404(Category, slug=slug)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:
            Post.objects.create(
                title=title,
                content=content,
                author=request.user,
                category=category
            )
            messages.success(request, 'Post created successfully!')
            return redirect('category_detail', slug=slug)
    
    return render(request, 'forum/create_post.html', {'category': category})


@login_required
def create_reply(request, post_id):
    """Create a reply to a post"""
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        
        if content:
            Reply.objects.create(
                post=post,
                author=request.user,
                content=content
            )
            messages.success(request, 'Reply added successfully!')
    
    return redirect('post_detail', post_id=post_id)
