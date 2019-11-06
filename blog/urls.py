from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name="list_blog"),
    path('single/<int:pk>', views.new_single, name="new_single"),
]
