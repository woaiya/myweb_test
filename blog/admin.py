from django.contrib import admin

# Register your models here.

from blog.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'title', 'timestamp']


admin.site.register(BlogPost, BlogPostAdmin)