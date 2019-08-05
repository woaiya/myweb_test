from django.db import models

# Create your models here.

from ckeditor.fields import RichTextField


class BlogPost(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, default='test', verbose_name='用户名')
    title = models.CharField(max_length=150, verbose_name='标题')
    # body = models.TextField()
    body = RichTextField(config_name='default', verbose_name='内容')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog'
        verbose_name = '博客'
        verbose_name_plural = verbose_name
