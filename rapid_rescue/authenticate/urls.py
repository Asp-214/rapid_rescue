
from django.contrib import admin
from django.urls import path , include
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('',views.redirection, name='redirection'),
    path('login/', views.user_login, name='login'),
    path('logout/' , views.user_logout, name = 'logout')

]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
