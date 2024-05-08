#%%
#authenticate views

from django.shortcuts import render, redirect 

from django.contrib.auth import authenticate, login,logout 
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required 
# Create your views here.


@login_required(login_url='login')
def redirection(request):
    return redirect('dashboard')

@never_cache
def user_login(request):

    user = None
    incorrect = False
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            incorrect = True
        # else:
        #     return render(request, 'login.html',{'success': False, 'message': 'Incorrect username or password'})

    return render(request,'authenticate/login.html', {'incorrect': incorrect })


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

#%%
#authenticate urls

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