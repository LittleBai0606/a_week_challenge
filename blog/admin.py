from django.contrib import admin
from .models import Category, Tag, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'created_time', 'modified_time', 'category']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
