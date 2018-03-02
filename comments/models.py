from django.db import models

# Create your models here.

class Comment(models.Model):

    name = models.CharField(max_length=50, verbose_name=u'姓名')
    email = models.EmailField(max_length=255, verbose_name=u'邮箱')
    url = models.URLField(blank=True, verbose_name=u'链接')
    text = models.TextField(verbose_name=u'内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=u'留言创建时间')

    post = models.ForeignKey('blog.Post', verbose_name=u'所属博文')

    def __str__(self):
        return self.text[:20]

