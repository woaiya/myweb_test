from django.shortcuts import render

# Create your views here.

from login.models import UserPost
from django.http import HttpResponse

from login.forms import UserAccountForm
import json


def index(request):
    if request.method == 'POST':
        userFrom = UserAccountForm(request.POST)
        if userFrom.is_valid():
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
        else:
            print(userFrom.errors)

            return render(request, 'login/index.html', {'error': userFrom.errors})
    return render(request, 'login/index.html')
