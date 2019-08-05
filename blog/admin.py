from django.contrib import admin

# Register your models here.

from blog.models import BlogPost, CategoryModels


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'title', 'category', 'views', 'blog_colored_status']


class CategoryModelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category_colored_status']


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(CategoryModels, CategoryModelsAdmin)
