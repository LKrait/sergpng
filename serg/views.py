from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    return render(request, 'serg/home.html')


#def about(request):
#    return render(request, 'serg/about.html')
#

#def contact(request):
#    return render(request, 'serg/contacts.html')


#def product(request):
#    return render(request, 'serg/products.html')


def index(request):
    return render(request, 'serg/index.html')
