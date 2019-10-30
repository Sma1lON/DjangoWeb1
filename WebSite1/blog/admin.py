from django.contrib import admin
from blog.models import blog, Category, Tag

admin.site.register(blog)
admin.site.register(Category)
admin.site.register(Tag)
