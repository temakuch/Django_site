from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Post

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def show_post(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'all_posts':posts})

def register(request):
    return render(request, 'register.html')