"""
AndroidServer Punch URL Configuration
"""
from django.contrib import admin
from django.urls import path
from . import views
# from django.conf.urls import url

urlpatterns = [
    path('form/', views.form),
    path('login/', views.login),
    path('postForm/', views.postForm)
    # path('username/', views.username),
    # path('password/', views.password),
]