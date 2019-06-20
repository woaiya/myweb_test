from django.db import models

# Create your models here.


class BlogPost(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, default='test')
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog'
        verbose_name = '博客'
        verbose_name_plural = verbose_name
