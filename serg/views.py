from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    return render(request, 'serg/home.html')


def index(request):
    return render(request, 'serg/index.html')
