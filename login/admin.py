from django.contrib import admin

# Register your models here.

from login.models import UserPost


class UserPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'update']


admin.site.register(UserPost, UserPostAdmin)