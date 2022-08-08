from django.shortcuts import render
from .models import Post


def forum(request):
    post = Post.objects.all()
    return render(request, 'forum/forum.html', {'posts': post})


def new_post(request):
    post = Post.objects.all()

    if request.method == 'GET':

        if request.GET.get("post_name"):
            post = Post.objects.filter(
                nombre__icontains=request.GET.get("post_name"))
            return render(request, "forum/forum.html", {'posts': post})
        else:
            return render(request, 'forum/new_post.html', {'posts': post})
    else:
        formulary = request.POST

        title = formulary.get("title")
        description = formulary.get("description")

        new_post = Post(title=title, description=description)
        new_post.save()

        return render(request, "forum/forum.html", {'posts': post})
