from django.urls import path
from .forms import NewPost,CommentForms
from .models import Blog
from . import views

urlpatterns = [
    path('', views.blog_list, name="list_blog"),
    path('single/<int:pk>', views.blog_detail, name="blog_detail"),
    path('single/<int:id>/edit', views.edit, {},name='edit_post'),
    path('single/new', views.post_new, name="post_new"),
    path('single/<int:id>/com/<int:cid>/edit', views.editcom, name="edit_com"),
    path('single/<int:id>/delete', views.delete, name="del_post"),
    path('single/<int:id>/com/<int:cid>/delete', views.deletecom, name="del_com")
]
