from django.urls import path
from .forms import NewPost,CommentForms
from .models import Blog
from . import views

urlpatterns = [
    path('', views.blog_list, name="list_blog"),
    path('single/<int:pk>', views.new_single, name="new_single"),
    path('single/edit/<int:id>', views.edit, {},name='edit_post'),
    path('single/new/', views.post_new, name="post_new"),
    path('single/edit/com/<int:pk>', views.edit_comments, name="edit_com"),
]
