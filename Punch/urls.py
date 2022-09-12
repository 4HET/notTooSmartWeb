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
    path('login/', views.login),
    path('insert/', testdb.insert),
    path('delete/', testdb.delete),
    path('index/', views.index),
    path('logout/', views.logout),
    path('order/', views.order),
    path('isPunch/', views.isPunch),

    # path('username/', views.username),
    # path('password/', views.password),
]