"""
AndroidServer Punch URL Configuration
"""
from django.contrib import admin
from django.urls import path
from . import views
# from django.conf.urls import url

urlpatterns = [
    path('punch/', views.postRequest),
    # path('username/', views.username),
    # path('password/', views.password),
]