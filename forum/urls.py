from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/new/', views.create_post, name='create_post'),
    path('post/<int:post_id>/reply/', views.create_reply, name='create_reply'),
]
