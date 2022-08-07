from urllib import request
from django.db import models
import datetime


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    creation_date = models.DateTimeField(default=datetime.date.today)
