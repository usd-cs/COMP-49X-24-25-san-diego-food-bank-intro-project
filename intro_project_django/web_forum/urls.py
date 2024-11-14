"""This module contains URL routing for the web forum application."""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("post/", views.post_view, name="post"),
    path("create_post/", views.create_post_view, name="create post"),
    path("single_post/", views.post_view, name="single post"),
    path("single_post/loaded_comments/", views.loaded_comments_view, name="loaded comments")
    # path("login/", views.login_view name="login")  Running into some sort of syntax error here
]
