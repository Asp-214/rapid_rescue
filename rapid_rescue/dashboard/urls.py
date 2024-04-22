from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('logout/',views.user_logout, name='logout'),
    path('', views.login_redirect, name='login_redirect')
]
 