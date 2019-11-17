from django.shortcuts import render
from .models import user, User, Category, Tag, blog
from django.shortcuts import get_object_or_404, reverse, render

from django.views.generic.edit import UpdateView, DeleteView, CreateView


# Create your views here.
