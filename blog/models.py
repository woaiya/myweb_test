from django.db import models

# Create your models here.

from django.utils.html import format_html
from ckeditor.fields import RichTextField


class CategoryModels(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=20, verbose_name='标题')
    state = models.IntegerField(default=1)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    """
    这个方法用来处理后台显示，当state状态为1时显示正常，否则显示异常
    category_colored_status.short_description 用来处理这个方法的标题显示
    """
    def category_colored_status(self):
        if self.state == 1:
            color_code = 'green'
            state_name = '正常'
        else:
            color_code = 'red'
            state_name = '异常'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            state_name,
        )
    category_colored_status.short_description = '状态'

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class BlogPost(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, default='test', verbose_name='用户名')
    title = models.CharField(max_length=150, verbose_name='标题')
    # body = models.TextField()
    body = RichTextField(config_name='default', verbose_name='内容')
    state = models.IntegerField(default=1, verbose_name='状态')
    # 关联表category
    category = models.ForeignKey(CategoryModels, default=1, on_delete=models.DO_NOTHING, verbose_name='分类')
    views = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def blog_colored_status(self):
        if self.state == 1:
            color_code = 'green'
            state_name = '正常'
        else:
            color_code = 'red'
            state_name = '异常'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            state_name,
        )
    blog_colored_status.short_description = '状态'

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog'
        verbose_name = '博客'
        verbose_name_plural = verbose_name
