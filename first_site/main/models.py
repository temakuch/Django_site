from django.db import models
from django.utils import timezone
# from django.contrib.auth.forms import UserCreationForm
# from django import forms

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_of_creation = models.DateTimeField(default = timezone.now)

    # def __str__(self):
    #     return f"New_post{self.title}"

# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         fields = ['username', 'password', 'password2', 'email']