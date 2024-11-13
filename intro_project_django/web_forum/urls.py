"""This module contains URL routing for the web forum application."""

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("post/", views.post_view, name="post"),
    path("create_post/", views.create_post_view, name="create post"),
    path("login/", views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
