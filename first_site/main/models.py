from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_of_creation = models.DateTimeField(default = timezone.now)

    # def __str__(self):
    #     return f"New_post{self.title}"