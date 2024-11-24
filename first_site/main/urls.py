from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('register/', views.register),
    path('post/', views.show_post)
]

