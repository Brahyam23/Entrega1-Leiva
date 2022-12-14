from django.shortcuts import render
from .models import Post


def forum(request):
    post = Post.objects.all()

    if request.GET.get("post_title"):

        post = Post.objects.filter(
            title__icontains=request.GET.get("post_title"))
        return render(request, "forum/forum.html", {'posts': post})

    else:
        return render(request, 'forum/forum.html', {'posts': post})


def new_post(request):
    post = Post.objects.all()

    if request.method == 'GET':
        return render(request, 'forum/new_post.html', {'posts': post})

    else:
        formulary = request.POST

        title = formulary.get("title")
        description = formulary.get("description")

        new_post = Post(title=title, description=description)
        new_post.save()

        return render(request, "forum/forum.html", {'posts': post})
