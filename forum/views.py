from django.shortcuts import render


def forum(request):
    return render(request, 'forum.html')


def new_notice(request):
    return render(request, 'new_notice.html')
