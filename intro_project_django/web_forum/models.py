"""Models defining the tables within Postgresql database"""
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """User table for storing information on admins and users"""
    email = models.EmailField(unique=True)
    admin = models.BooleanField(default=False)

class Post(models.Model):
    """Post table for storing information for posts"""
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts')
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    """Comment table for storign information for comments"""
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='comments')
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
