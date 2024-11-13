from django.urls import path
from . import views
"""Temp docstring for linting"""
urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.posts, name="posts"),
    path("post/", views.post, name="post"),
]