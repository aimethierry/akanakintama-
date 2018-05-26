from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=140, blank=True, null=True)
    text = models.TextField()
    image = models.FileField(upload_to='media/', blank=True, null=True)
    image1 = models.FileField(upload_to='media/', blank=True, null=True)
    image2 = models.FileField(upload_to='media/', blank=True, null=True)
    image3 = models.FileField(upload_to='media/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Blog, null=True, blank=True)
    name = models.CharField(max_length=140)
    email = models.CharField(max_length=140)
    text = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.name
