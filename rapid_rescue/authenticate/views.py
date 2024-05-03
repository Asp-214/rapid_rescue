from django.shortcuts import render, redirect
from django.http import HttpResponse , JsonResponse
from django.contrib.auth import authenticate, login, logout 
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required 
from users.models import CustomUser


# Base Empty Redirection if Logged in
@login_required(login_url='login')
def redirector(request):
    return redirect('dashboard')


# For Rendering Login Page
@never_cache
def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'login/login.html')


# For Authentication with AJAX
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            CustomUser.objects.get(username=username) # if not exists it throws an exception
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                status = 0
            else:
                status = 1
        except CustomUser.DoesNotExist:
            status = -1
            
        data = { 'status' : status }
        return JsonResponse( data ,status=200 )
    else:
        return HttpResponse(request ,"Error : Access Denied ") 


# For Logging out / Clearing Sessions
def user_logout(request):
    logout(request)
    return redirect('login')