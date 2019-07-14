from django.shortcuts import render, redirect, reverse

# Create your views here.

from login.models import UserPost
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'login/index.html')


@csrf_exempt
def ajax_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = UserPost.objects.filter(username=username, password=password)
    if user:
        msg = {"code": 200, "msg": ""}
        request.session['is_login'] = True
        request.session['user_id'] = username
    else:
        msg = {"code": 400, "msg": "用户名密码错误"}
    return JsonResponse(msg)


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        UserPost.objects.create(username=username, password=password)
        return redirect(reverse('blog:index'))
    return render(request, 'login/registration.html')


def logout(request):
    if not request.session.get('is_login', None):
        return redirect(reverse('login:index'))
    request.session.flush()
    return redirect(reverse('login:index'))
