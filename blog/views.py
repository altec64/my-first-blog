
#blog in app views

from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    #Create queryset, filter post now, sor by first published date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')       

    #def render(request, template_name, context=None, content_type=None, status=None, using=None)
    return render(request,'blog/post_list.html',{'posts':posts})
    