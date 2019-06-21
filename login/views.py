from django.shortcuts import render

# Create your views here.

from login.models import UserPost
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if UserPost.objects.filter(username=username).exists():
            user = UserPost.objects.get(username=username)
            if password == user.password:
                return HttpResponse('登录成功')
            else:
                return HttpResponse('账号密码错误')
        else:
            return HttpResponse('用户不存在')
    return render(request, 'login/index.html')
