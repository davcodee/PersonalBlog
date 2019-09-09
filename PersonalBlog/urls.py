from django.contrib import admin
from django.urls import path
from home import views as home_posts


urlpatterns = [
    path('home/',home_posts.list_posts),
    path('aboutme/',home_posts.aboutme),
]
