#blog in app views
from django.shortcuts import render

# Create your views here.

def post_list(request):
    #def render(request, template_name, context=None, content_type=None, status=None, using=None)
    return render(request,'blog/post_list.html',{})
    