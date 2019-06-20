from django.shortcuts import render, redirect, reverse

# Create your views here.

from blog.models import BlogPost
from django.views.decorators.csrf import csrf_exempt


def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def body(request, body_id):
    posts = BlogPost.objects.get(id=body_id)
    return render(request, 'blog/body.html', {'posts': posts})


@csrf_exempt
def add(request):
    if request.method == "POST":
        BlogPost.objects.create(title=request.POST['title'], body=request.POST['body'])
        return redirect(reverse('blog:index'))
    return render(request, 'blog/add.html')


@csrf_exempt
def edit(request, body_id):
    if request.method == "POST":
        BlogPost.objects.filter(id=body_id).update(title=request.POST['title'], body=request.POST['body'])
    posts = BlogPost.objects.get(id=body_id)
    return render(request, 'blog/edit.html', {'posts': posts})


# 删除方法
def delete(request, body_id):
    BlogPost.objects.filter(id=body_id).delete()
    return redirect(reverse('blog:index'))

