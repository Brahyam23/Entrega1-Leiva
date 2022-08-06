from urllib import request
from django.db import models


class User(models.Model):
    nombre = models.CharField(max_length=255)
    nick = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    creation_date = models.DateField()
