from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index-page'),
    #path('about/', views.about, name='about-us'),
    #path('contacts/', views.contact, name='contact-us'),
    #path('products/', views.product, name='our-products'),
    #path('index/', views.index, name='index-page'),
    #path('login/', views.login, name='user-login'),
    #path('dashboard/', views.dashboard, name='dashboard'),
]
