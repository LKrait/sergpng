from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm


def index(request):
    return render(request, 'serg/index.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Get the data from the form submitted

        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('index-page')  # Redirect to the homepage or dashboard
            else:
                messages.error(request, 'Invalid username or password')

    else:
        form = LoginForm()  # Display an empty form for GET requests

    return render(request, 'serg/login.html', {'form': form})