from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Tag, Post

# Create your views here.

class IndexView(View):
    """
    首页
    """

    def get(self, request):
        post_list = Post.objects.all()
        return render(request, 'blog/index.html',
                      context={'post_list': post_list})


class DetailView(View):

    def get(self, request, blog_id):
        post = get_object_or_404(Post, pk=blog_id)
        return render(request, 'blog/detail.html',
                      context={'post': post})
