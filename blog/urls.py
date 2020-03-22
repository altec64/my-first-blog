#blog in app url.py
from django.urls import path

#from blog app import blog app views
from . import views

urlpatterns= [
    path('', views.post_list, name='post_list'),
    # <int:pk> means that Django expects an integer value 
    # and will transfer it to a view as a variable called pk.
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]
