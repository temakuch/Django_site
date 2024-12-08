from django.shortcuts import render, get_object_or_404
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

def show_one_post(request, post_id):
    _post = get_object_or_404(Post, id = post_id)
    return render(request, 'one_post.html', {'post':_post})

def register(request):
    err = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            err = form.errors.as_data()
    form = UserCreationForm
    return render(request, 'register.html', {"form":form})