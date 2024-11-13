"""Temp docstring for linting"""

from django.http import HttpResponse

# Create your views here.
def index():
    """Handle the home/login page."""
    return HttpResponse("This is the home/login page.")

def posts():
    """Handle the posts page."""
    return HttpResponse("This is the posts page.")

def post():
    """Handle viewing a specific post by its ID."""
    return HttpResponse("This is a path to see a specific post (postID/post/)")
