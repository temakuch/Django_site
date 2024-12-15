from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
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
            username = form.cleaned_data.get("username")
            messages.success(request, f"Новий аккаунт було успішно створено: {username}")
            login(request, user)
            return redirect("/")
        else:
            err = form.errors.as_data()
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
    form = UserCreationForm
    return render(request, 'register.html', {"form":form, "error":err})

def user_login(request):
    islogin = request.user.is_authenticated
    if request.method == "POST":
        a_form = AuthenticationForm(request, data=request.POST)
        if a_form.is_valid():
            username = a_form.cleaned_data.get("username")
            password = a_form.cleaned_data.get("password")
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Ви залогінились під іменем {username}")
                return redirect("/")
            else:
                messages.error(request, "Користувач з таким логіном та паролем не знайдено")
        else:
            messages.error(request, "Пароль або логін неправильні")
    a_form = AuthenticationForm
    return render(request, "login.html", {"form":a_form, "islogin":islogin})

def user_logout(request):
    logout(request)
    messages.info(request, "Ви вийшли з аккаунта")
    return redirect("/")
