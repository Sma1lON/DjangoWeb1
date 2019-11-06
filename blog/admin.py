from django.contrib import admin
from blog.models import Blog, Category, Tag, Comments

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')


admin.site.register(Comments, CommentAdmin)
