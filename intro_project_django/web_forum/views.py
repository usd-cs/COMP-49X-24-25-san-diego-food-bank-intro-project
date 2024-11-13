"""Temp docstring for linting"""

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    """
    Properly handle user login by displaying the login form and processing the user authentication.

    This view will display the login form for users to input their email and password. It will validate
    the user's credentials and log them in where they will be redirected to the home page.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def header(response):
    return render(response, "main/header.html", {})

def home_view(response):
    """Placeholder view for the home page."""
    return render(response, "main/home.html", {})

def post_view():
    """Placeholder view for viewing a post."""
    return HttpResponse("This is a post view.")

def create_post_view():
    """Placeholder view for creating a new post."""
    return HttpResponse("This is the create post view.")