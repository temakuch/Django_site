from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def show_post(request):
    
    return(request, 'post.html')

def register(request):
    return render(request, 'register.html')