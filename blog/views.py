# blog/views.py
from django.shortcuts import render
from .models import Post  # ← Article から Post に変更

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
