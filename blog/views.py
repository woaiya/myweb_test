from django.shortcuts import render, redirect, reverse

# Create your views here.

from blog.models import BlogPost


def index(request):
    posts = BlogPost.objects.filter(state=1)
    return render(request, 'blog/index.html', {'posts': posts})


def body(request, body_id):
    posts = BlogPost.objects.get(id=body_id)
    # 浏览量增加
    BlogPost.objects.filter(id=body_id).update(views=posts.views+1)
    return render(request, 'blog/body.html', {'posts': posts})


def add(request):
    if request.method == "POST":
        BlogPost.objects.create(title=request.POST['title'], body=request.POST['body'])
        return redirect(reverse('blog:index'))
    return render(request, 'blog/add.html')


def edit(request, body_id):
    if request.method == "POST":
        BlogPost.objects.filter(id=body_id).update(title=request.POST['title'], body=request.POST['body'])
    posts = BlogPost.objects.get(id=body_id)
    return render(request, 'blog/edit.html', {'posts': posts})


# 删除方法
def delete(request, body_id):
    # 假删除
    BlogPost.objects.filter(id=body_id).update(state=0)
    # 真删除
    # BlogPost.objects.filter(id=body_id).delete()
    return redirect(reverse('blog:index'))
