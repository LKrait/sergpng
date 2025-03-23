from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index-page'),
    path('login/', views.login_view, name='login' ),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('messages/', views.user_messages, name='user-messages'),
    path('settings/', views.user_settings, name='user-settings'),
    path('logout/', views.logout, name='logout'),
    path('vp/', views.viewpage, name='viewpage')
]
