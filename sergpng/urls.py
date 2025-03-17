from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views


urlpatterns = [
    path('bosstumas/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('', include('serg.urls')),
]
