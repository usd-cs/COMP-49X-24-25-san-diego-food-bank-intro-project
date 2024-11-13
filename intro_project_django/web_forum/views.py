"""Temp docstring for linting"""

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    """
    Handle user login by displaying login form and processing user authentication.

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

def home_view():
    """Placeholder view for the home page."""
    return HttpResponse("Welcome to the home page.")

def post_view():
    """Placeholder view for viewing a post."""
    return HttpResponse("This is a post view.")

def create_post_view():
    """Placeholder view for creating a new post."""
    return HttpResponse("This is the create post view.")
