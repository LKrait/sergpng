from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from .models import SiteVisit
from django.contrib.auth.decorators import login_required


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
                return redirect('viewpage')  # Redirect to the homepage or dashboard
            else:
                messages.error(request, 'Invalid username or password')

    else:
        form = LoginForm()  # Display an empty form for GET requests

    return render(request, 'serg/login.html', {'form': form})


@login_required
def viewpage(request):
    return render(request, 'serg/dashboard.html')


@login_required
def dashboard(request):
    content = {
        'title': 'Dashboard',
        'body': 'This is your Dashboard. Here you can manage your activities and view important stats.'
    }
    return JsonResponse(content)

@login_required
def profile(request):
    site_visit = SiteVisit.objects.first()

    if not site_visit:
        site_visit = SiteVisit.objects.create(visit_count=0)

    data = {
        'title': 'Profile',
        'body': f"Current Site Visit Count: {site_visit.visit_count} <br>Last Visit On: {site_visit.last_visit}",
        'visit_count': site_visit.visit_count
    }
    
    return JsonResponse(data)

@login_required
def user_messages(request):
    content = {
        'title': 'Messages',
        'body': 'Here are your messages. Check your inbox for updates and conversations.'
    }
    return JsonResponse(content)


@login_required
def user_settings(request):
    content = {
        'title': 'Settings',
        'body': 'Manage your account and application settings here.'
    }
    return JsonResponse(content)

@login_required
def logout(request):
    content = {
        'title': 'Logout',
        'body': 'You have logged out. Please log in again to continue.'
    }
    return JsonResponse(content)