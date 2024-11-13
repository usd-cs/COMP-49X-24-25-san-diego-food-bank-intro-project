from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return render(response, "main/header.html", {})
def home(response):
    return render(response, "main/home.html", {})
def posts(response):
    return HttpResponse("This is the posts page.")
def post(response):
    return HttpResponse("This is a path to see a specific post (postID/post/)")