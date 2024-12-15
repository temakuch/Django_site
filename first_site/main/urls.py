from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('register/', views.register),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name = "logout"),
    path('post/', views.show_post),
    path('post/<int:post_id>', views.show_one_post, name='one_post')
]

