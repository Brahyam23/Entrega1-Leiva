from django.shortcuts import render
from .models import User


def new_user(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    else:
        formulary = request.POST

        name = formulary.get("name")
        username = formulary.get("username")
        password = formulary.get("password")
        email = formulary.get("email")

        user = User(name=name, username=username,
                    password=password, email=email)
        user.save()

        return render(request, "user/login.html")


def login(request):
    return render(request, 'user/login.html')
