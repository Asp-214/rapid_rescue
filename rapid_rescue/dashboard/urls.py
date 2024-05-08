
from django.contrib import admin
from django.urls import path , include
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('',views.user_dashboard, name='dashboard'),
    path('base/',views.base_test, name='base'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
