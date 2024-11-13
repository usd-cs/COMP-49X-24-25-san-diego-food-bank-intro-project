"""Temp docstring for linting"""

from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

def login_view(request):
    """
    Properly handle user login by displaying the login form and processing the user authentication.

    This view will display the login form for users to input their email and password. It will validate
    the user's credentials and log them in where they will be redirected to the home page.
    """
    if request.method == 'POST': # Make sure the request is 'POST' to ensure user submits form to be processed
        form = AuthenticationForm(data = request.POST) 
        if form.is_valid(): 
            user = form.get_user() # Retrieve the user if form is valid
            login(request, user) 
            return redirect('home')
    return render(request, 'login.html', {'form': form})

def home_view(request):
    pass # Setup later

def post_view(request):
    pass # Setup later

def create_post_view(request):
    pass # Setup later