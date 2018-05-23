from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=140, blank=True, null=True)
    text = models.TextField()
    image = models.FileField(upload_to='media/', blank=True, null=True)
    

    def __str__(self):
        return self.title