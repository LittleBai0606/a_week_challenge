from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import CommentForm
from blog.models import Post
from .models import Comment
from django.views import View

# Create your views here.

class CommentView(View):

    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context ={
                'post': post,
                'form': form,
                'comment_list': comment_list,
            }
            return render(request, 'blog/detail.html', context=context)

    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        return redirect(post)





