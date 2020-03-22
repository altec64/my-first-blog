#blog in app url.py
from django.urls import path
from . import views #from blog app import blog app views

urlpatterns= [
    path('', views.post_list, name='post_list'),
]
