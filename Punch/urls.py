"""
AndroidServer Punch URL Configuration
"""
from django.contrib import admin
from django.urls import path
from . import views, testdb

# from django.conf.urls import url

urlpatterns = [
    path('punch/', views.postRequest),
    path('select/', testdb.select),
    path('insert/', testdb.insert),
    path('delete/', testdb.delete),

    # path('username/', views.username),
    # path('password/', views.password),
]