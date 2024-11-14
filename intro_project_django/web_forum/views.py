"""Temp docstring for linting"""

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    """
    Properly handle user login by displaying the login form and processing the user authentication.

    This view will display the login form for users to input their email and password. It will
    validate the user's credentials and log them in, then redirect them to the home page.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'web_forum/login.html', {'form': form})

def navigation_bar(request):
    """Contains the html data for the navigation bar."""
    return render(request, "web_forum/navigation_bar.html", {})

def home_view(request):
    """Placeholder view for the home page."""
    return render(request, "web_forum/home.html", {})

def post_view(request):
    """Placeholder view for viewing a post."""
    return render(request, HttpResponse("This is a post view."))

def create_post_view(request):
    """Page for creating a new post. The add post button adds the 
    inputted text to the database as a post object. Return to home
    page after adding post."""
    # if request.method == 'POST':
    #     content = request.POST.get('content')
    #     if content:
    #         Post.objects.create(content=content)
    #         return redirect('home')  # Redirect to home page after creating a post
    # Render the create post page if GET request
    return render(request, 'web_forum/create_new_post.html')
