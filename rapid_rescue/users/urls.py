from django.urls import path , include
from . import views

# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('',views.show_users,name='users'),
    path('create/', views.create_user,name='create_user'),
    path('modify/', views.modify_user)

]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
