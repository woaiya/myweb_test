from django.shortcuts import render

# Create your views here.

from login.models import UserPost
from django.http import HttpResponse

from login.forms import UserAccountForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return render(request, 'login/index.html')


@csrf_exempt
def ajax_login(request):
    username = request.POST['username']
    password = request.POST['password']
    if username == 'admin' and password == '123456':
        msg = {"code": 200, "msg": ""}
    else:
        msg = {"code": 400, "msg": "用户名密码错误"}
    return JsonResponse(msg)