from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name=u'分类')

    def __str__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField(max_length=100, verbose_name=u'标签')

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=70, verbose_name=u'标题')

    body = models.TextField(verbose_name=u'正文')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    modified_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')

    excecpt = models.CharField(max_length=200, blank=True, verbose_name=u'摘要')

    category = models.ForeignKey(Category, verbose_name=u'文章分类')

    tag = models.ManyToManyField(Tag, verbose_name=u'文章标签')

    author = models.ForeignKey(User, verbose_name=u'文章作者')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'blog_id': self.pk})

