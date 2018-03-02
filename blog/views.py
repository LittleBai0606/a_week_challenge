from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views import View
from .models import Category, Tag, Post
import markdown
from .forms import AddForm, CommentForm

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
    """
    博客详情页面
    """

    def get(self, request, blog_id):
        post = get_object_or_404(Post, pk=blog_id)
        post.body = markdown.markdown(post.body, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        form = CommentForm
        comment_list = post.comment_set.all()
        return render(request, 'blog/detail.html',
                      context={
                        'post': post,
                        'form': form,
                        'comment_list': comment_list,
                      })


class ArchivesView(View):
    """
    归档
    """
    def get(self, request, year, month):
        post_list = Post.objects.filter(
            created_time__year=year, created_time__month=month)
        return render(request, 'blog/index.html', context={'post_list': post_list})


class CategoryView(View):
    """
    分类
    """
    def get(self, request, category_id):
        cate = get_object_or_404(Category, pk=category_id)
        post_list = Post.objects.filter(category=cate)
        return render(request, 'blog/index.html', context={'post_list': post_list})


class TestView(View):

    def post(self, request):
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(int(a)+int(b))
        return render(request, 'blog/test.html',
                      context={'form': form})

    def get(self, request):
        form = AddForm()
        return render(request, 'blog/test.html',
                      context={'form': form})








