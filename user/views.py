from django.shortcuts import render


def new_user(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')
