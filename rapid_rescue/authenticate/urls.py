from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirector, name='redirector'),
    path('login/',views.login_page, name='login'),
    path('login/auth/verify/', views.user_login, name='authverify' ),
    path('logout/' , views.user_logout, name = 'logout')
]