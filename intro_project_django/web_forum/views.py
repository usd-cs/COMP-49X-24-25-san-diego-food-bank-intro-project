from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("This is the home/login page.")
def posts(response):
    return HttpResponse("This is the posts page.")
def post(response):
    return HttpResponse("This is a path to see a specific post (postID/post/)")