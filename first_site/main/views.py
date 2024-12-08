from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
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
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            err = form.errors.as_data()
    form = UserCreationForm
    return render(request, 'register.html', {"form":form, "error":err})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username, password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, "login.html")
