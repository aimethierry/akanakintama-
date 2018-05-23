from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=140, blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        self.title


class Image(models.Model):
    image = models.FileField(upload_to='media/', blank=True, null=True)
    post = models.ForeignKey(Post, default=None)