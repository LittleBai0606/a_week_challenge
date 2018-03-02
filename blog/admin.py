from django.contrib import admin
from .models import Category, Tag, Post
from comments.models import Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'created_time', 'modified_time', 'category']
    search_fields = ['title', ]


class PostComment(admin.ModelAdmin):
    list_display = ['name', 'text', 'url', 'created_time']



admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, PostComment)
