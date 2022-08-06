from django.urls import path
from forum.views import *

urlpatterns = [
    path('', forum, name='forum'),
    path('new_notice', new_notice, name='new_notice')
]
